import logging

import imagehash
import time
import json
import re
import redis
import datetime
import os
import requests
from PIL import Image
from io import BytesIO
from collections import defaultdict
from operator import itemgetter

# logger = logging.getLogger('django.time')

logger = logging.getLogger('django')
handler = logging.FileHandler('log.log')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

with open('../dja/db.json') as f:
    # redis_key = json.loads(f.read())['REDIS_KEY']
    redis_key = json.loads(f.read())['REDIS_KEY_LOCAL']

pool = redis.ConnectionPool(host=redis_key['host'], port=redis_key['port'],
                            decode_responses=redis_key['decode_responses'], password=redis_key['password'],
                            db=1)

Reds = redis.Redis(connection_pool=pool)


def hamming(value1, value2):
    difference = (int(value1, 16)) ^ (int(value2, 16))
    return bin(difference).count("1")


def search_image(data):
    pre_start_time = time.time()
    banlist = Reds.smembers('banlist')
    # redis所有hash值:
    try:
        images = data.getlist('images')
    except:
        images = data['images']
    local_hash = Reds.hgetall('imagehash')
    # redis所有id值:
    local_id = Reds.hvals('imagehash')
    pre_end_time = time.time()
    logger.info(json.dumps({'total_time:': pre_end_time - pre_start_time}))
    # 遍历post过来的图片列表
    results = {}
    results['pid'] = data['pid']
    hash_value_list = [data['pid'], ]
    similar_rate_dict = defaultdict(list)
    # imagehashs = []
    # rvs_imagehashs= []
    down_time_list = []
    cal_time_list = []
    for img in images:
        down_start_time = time.time()
        resp = requests.get(img).content
        image = Image.open(BytesIO(resp))
        down_end_time = time.time()
        rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        # 对图片进行hash
        image_hash = str(imagehash.phash(image))
        rvs_image_hash = str(imagehash.phash(rvs_image))
        cal_start_time = time.time()
        if image_hash in banlist or rvs_image_hash in banlist:
            continue
        hash_value_list.append(image_hash)
        if local_hash:
            # 遍历
            for hash_values in local_hash:
                try:
                    j_hash_values = json.loads(hash_values)[1:]
                except:
                    continue
                for hash_value in j_hash_values:
                    if str(hash_value) == image_hash or str(hash_value) == rvs_image_hash:
                        rate_zip = 1
                        similar_rate_dict[Reds.hget('imagehash', hash_values)] = rate_zip
        cal_end_time = time.time()
        down_time_list.append(down_end_time - down_start_time)
        cal_time_list.append(cal_end_time - cal_start_time)
    logger.info(json.dumps({'total_time:': sum(down_time_list), 'down_time_list:': down_time_list}))
    logger.info(json.dumps({'total_time:': sum(cal_time_list), 'cal_time_list:': cal_time_list}))
    # similar_rate = round(1 - hamming(hash_value, image_hash) / 64, 3)
    # rvs_similar_rate = round(1 - hamming(hash_value, rvs_image_hash) / 64, 3)
    # if similar_rate > 0.85 or rvs_similar_rate > 0.85:
    #     rate_zip = [similar_rate, rvs_similar_rate]
    #     similar_rate_dict[Reds.hget('imagehash', hash_values)].append(rate_zip)

    if str(data['pid']) not in local_id:
        hash_value_list = json.dumps(hash_value_list)
        Reds.hset('imagehash', hash_value_list, data['pid'])
        try:
            Reds.hset('reverse', data['pid'], hash_value_list)
        except:
            pass

    if not results:
        results = {"pid": data['pid'], "similar_rate": 0}
        return results
    # similar_rate_list.sort(key=itemgetter('rate', 'pid'), reverse=True)
    results['similar_rate'] = json.dumps(similar_rate_dict)
    # print(results)
    return results


def del_pic(pic_list):
    failed_list = []
    for img in pic_list:
        resp = requests.get(img).content
        image = Image.open(BytesIO(resp))
        image_hash = str(imagehash.phash(image))
        all_key = Reds.hgetall('imagehash')
        success = 0
        for key in all_key:
            if image_hash in eval(key):
                key_list = eval(key)
                key_list.remove(image_hash)
                print(key)
                Reds.hdel('reverse', all_key[key])
                Reds.hdel('imagehash', key)
                Reds.hset('reverse', key_list[0], json.dumps(key_list))
                Reds.hset('imagehash', json.dumps(key_list), key_list[0])
                success += 1
        if success == 0:
            failed_list.append('{0}删除失败'.format(img))
    return failed_list


def search_pic(img):
    resp = requests.get(img).content
    image = Image.open(BytesIO(resp))
    image_hash = str(imagehash.phash(image))
    all_pid = Reds.hget('imagehash', image_hash)
    print(all_pid)
    return all_pid


def view_banlist():
    banlist = list(Reds.smembers('banlist'))
    return banlist


def add_to_banlist(img_list):
    status_list = []
    for img in img_list:
        resp = requests.get(img).content
        image = Image.open(BytesIO(resp))
        image_hash = str(imagehash.phash(image))
        status = Reds.sadd('banlist', image_hash)
        status_list.append('{0}的拉黑结果:{1}'.format(img, status))
    return status_list


def del_from_banlist(img_list):
    status_list = []
    for img in img_list:
        resp = requests.get(img).content
        image = Image.open(BytesIO(resp))
        image_hash = str(imagehash.phash(image))
        status = Reds.srem('banlist', image_hash)
        status_list.append('{0}的解除黑名单结果:{1}'.format(img, status))
    return status_list


if __name__ == '__main__':
    a = {'images': [
        'http://gi.esmplus.com/pkw8088/shoes/g-loafer/revmin-14800.jpg',
        'http://gi.esmplus.com/pkw8088/shoes/g-loafer/etude-s-14800.jpg',
        'http://gi.esmplus.com/pkw8088/shoes/g-loafer/moonmoon-14800.jpg',
        'http://gi.esmplus.com/pkw8088/shoes/g-loafer/cozy-19800.jpg',
        'http://gi.esmplus.com/pkw8088/shoes/g-loafer/clyti-19800.jpg',
    ],
        'pid': 1000005
    }
    search_pic('http://gi.esmplus.com/pkw8088/shoes/g-loafer/clyti-19800.jpg')
    # search_image(a)
