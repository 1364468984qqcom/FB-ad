# -*- coding: utf-8 -*-

import logging
import imagehash
from PIL import Image
import json
import time
import requests
import redis
from io import BytesIO

logger = logging.getLogger('django.time')

with open('D:\WorkProject\ImageProject\PicRec\dja\db.json') as f:
    redis_key = json.loads(f.read())['REDIS_KEY']

pool = redis.ConnectionPool(host=redis_key['host'], port=redis_key['port'], passward=redis_key['password'],
                            decode_responses=redis_key['decode_responses'], db=redis_key['db'])

Red = redis.Redis(connection_pool=pool)


# 求汉明距离
def hamming(value1, value2):
    diffence = (int(value1, 16)) ^ (int(value2, 16))
    return bin(diffence).count('1')


def down_and_hash(img):
    """
    1.对图像进行下载和哈希
    :param img:
    :return:
    """
    try:
        res = requests.get(img).content
        image = Image.open(BytesIO(res))

        # 使用感知哈希去对图片进行相似度去重
        # ImageHash主要用于计算图像hash值，值为16进制数，可用于图像相似度匹配。
        image_hash = str(imagehash.phash(image))

        return image, image_hash
    except Exception:
        return "", ""


def search_image(data):
    try:
        images = data.getlist('images')
    except Exception:
        images = data['images']
    pre_start_time = time.time()
    banList = Red.smembers('banlist')
    pre_end_time = time.time()
    logger.info(json.dumps({f'{data["pid"]}--invoke_total_time:': pre_end_time - pre_start_time}))
    hash_value_list = []
    down_time_list = []
    cal_time_list = []
    similar_rate = {}

    for img in images:  # 遍历传进来的图片url
        down_start_time = time.time()
        # 下载图片
        image, image_hash = down_and_hash(img)
        down_end_time = time.time()
        rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        rvs_image_hash = str(imagehash.phash(rvs_image))
        if image_hash in banList or rvs_image_hash in banList:
            continue
        hash_value_list.append(image_hash)
        cal_start_time = time.time()

        # 判断如果单个哈希在'imagehash'的key里,找出对应的ID加入字典

        # hexists查看哈希表 key 中，指定的字段是否存在
        if Red.hexists('imagehash', image_hash) or Red.hexists('imagehash', rvs_image_hash):
            if Red.hexists('imagehash', image_hash):
                similar_ids = Red.hget('imagehash', image_hash)
                # HGET :获取存储在哈希表中指定字段的值。
            else:
                similar_ids = Red.hget('imagehash', rvs_image_hash)

            similar_ids = set(json.loads(similar_ids))
            rates = {pid: 1 for pid in similar_ids}
            similar_ids.add(int(data['pid']))
            similar_ids = list(similar_ids)
            if len(similar_ids) >= 10:
                # HSET :将哈希表 key 中的字段 field 的值设为 value 。
                Red.hset('duplicate_10', image_hash, img)
            Red.hset('imagehash', image_hash, json.dumps(similar_ids))
            similar_rate.update(rates)
        else:
            Red.hset('imagehash', image_hash, json.dumps([int(data['pid'])]))
        cal_end_time = time.time()
        down_time_list.append(down_end_time - down_start_time)
        cal_time_list.append(cal_end_time - cal_start_time)
    logger.info(
        json.dumps({f'{data["pid"]}--down_total_time:': sum(down_time_list), 'down_time_list:': down_time_list}))

    logger.info(
        json.dumps({f'{data["pid"]}--cal_total_time:': sum(cal_time_list), 'cal_time_list:': cal_time_list})
    )
    similar_rate = json.dumps(similar_rate)
    results = {'pid': int(data['pid']), 'similar_rate': similar_rate}
    # json.dumps() 用于将dict类型的数据转成str
    Red.hset('reverse', data['pid'], json.dumps(hash_value_list))
    logger.info(json.dumps(results))
    return results


def del_pic(pic_list):
    failed_list = []
    for img in pic_list:
        _, image_hash = down_and_hash(img)
        pids = Red.hget('imagehash', image_hash)
        if not pids:
            failed_list.append('{}删除失败'.format(img))
            continue
        pids = json.loads(pids)  # json.loads()用于将str类型的数据转成dict。
        Red.hdel('imagehash', image_hash)  # Redis Hdel 命令用于删除哈希表 key 中的一个或多个指定字段，不存在的字段将被忽略
        for pid in pids:
            hash_key = json.loads(Red.hget('reverse', pid))
            try:
                hash_key.remove(image_hash)
            except Exception:
                failed_list.append("{}删除失败".format(img))
                continue
            if not hash_key:
                Red.hdel('reverse', pid)
            else:
                Red.hset('reverse', pid, json.dumps(hash_key))
    if not failed_list:
        return '全部删除成功'
    return failed_list


def search_pic(imgs):
    """
    1.搜搜图片
    :param imgs:
    :return:
    """
    data = {}
    banlist = Red.smembers('banlist')
    for img in imgs:
        if img.startswith('http://') or img.startswith('https://'):
            _, image_hash = down_and_hash(img)
        else:
            image_hash = img
        if image_hash in banlist:
            data[img] = []
        else:
            all_pid = Red.hget('imagehash', image_hash)
            if all_pid:
                data[img] = json.loads(all_pid)
            else:
                data[img] = []
    return data


def cal_imagehashs(imgs):
    hashs = {}
    for img in imgs:
        _, image_hash = down_and_hash(img)
        hashs[img] = image_hash
    return hashs


def cal_imagehash(img):
    _, image_hash = down_and_hash(img)
    return image_hash


def add_to_banlist(img_lsit):
    status_list = []
    for img in img_lsit:
        dic = dict()
        image, image_hash = down_and_hash(img)
        rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        rvs_image_hash = str(imagehash.phash(rvs_image))
        status1 = Red.sadd('banlist', image_hash)
        status2 = Red.sadd('banlist', rvs_image_hash)
        Red.hdel('duplicate_10', image_hash)
        Red.hdel('duplicate_10', rvs_image_hash)
        result = [
            {'hash': image_hash, 'status': status1},
            {'hash': rvs_image_hash, 'status': status2}
        ]
        dic['url'] = img
        dic['result'] = result
        status_list.append(dic)
    return status_list


def def_from_banlist(img_list):
    status_list = []
    for img in img_list:
        _, image_hash = down_and_hash(img)

        # Redis Srem 命令用于移除集合中的一个或多个成员元素，不存在的成员元素会被忽略
        status = Red.srem('banlist', image_hash)
        status_list.append('{}的解除黑名单结果如下：{}'.format(img, status))
    return status_list


def query_dup_get_num(pk=10):
    d = dict()
    banlist = list(Red.smembers('banlist'))
    data = Red.hgetall('imagehash')  # 获取在哈希表中指定 key 的所有字段和值
    for k, v in data.items():
        v = json.loads(v)
        try:
            if len(v) >= int(pk) and k not in banlist:
                d.update({k: v})
        except Exception:
            continue

    return d


def query_dup(datas):
    ha = datas.get('hash')
    try:
        data = datas.getlist('image')
    except Exception:
        data = datas.get('image')

    for i in data:
        try:
            images = data.getlist(i)
        except Exception:

            images = data.get(i)

        # 遍历传来的图片url
        for img in images:

            # 下载图片以及给图片添加感知哈希
            image, image_hash = down_and_hash(img)
            rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            rvs_image_hash = str(imagehash.phash(rvs_image))
            if str(ha) == image_hash or str(ha) == rvs_image_hash:
                return {ha: img}
    return {ha: None}


def query_all_duplicate():
    d = Red.hgetall('duplicate_10')
    if not isinstance(d, dict):
        d = json.loads(d)
    data = []
    for i in d:
        data.append({'hash': 1, 'image': d[i], 'ids': json.loads(Red.hget('imagehash', i))})
    return data


if __name__ == '__main__':
    pic = 'http://pic1.win4000.com/pic/0/2a/2d71b4d188.jpg'
