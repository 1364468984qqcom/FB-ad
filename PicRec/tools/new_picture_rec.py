import logging
import imagehash
import time
import json
import redis
import requests
from PIL import Image
from io import BytesIO

logger = logging.getLogger('django.time')

# 取得绝对路径
with open('D:\WorkProject\ImageProject\PicRec\dja\db.json') as f:
    redis_key = json.loads(f.read())['REDIS_KEY']

    # 若要讲数据储存在本地redis，则将下面的注释去掉
    # redis_key = json.loads(f.read())['REDIS_KEY_LOCAL']  # 如需链接本地redis，将注释去掉

# 数据若储存本地文件，要改成自己的redis接口
pool = redis.ConnectionPool(host=redis_key['host'], port=redis_key['port'], password=redis_key['password'],
                            decode_responses=redis_key['decode_responses'], db=redis_key['db'])

Reds = redis.Redis(connection_pool=pool)


# 汉明距离为64个二进制数字
def hamming(value1, value2):
    difference = (int(value1, 16)) ^ (int(value2, 16))
    return bin(difference).count("1")


# 对图片进行下载和哈希
def down_and_hash(img):
    try:
        resp = requests.get(img).content
        image = Image.open(BytesIO(resp))
        # phash :感知哈希
        image_hash = str(imagehash.phash(image))  # ImageHash主要用于计算图像hash值，值为16进制数，可用于图像相似度匹配。
        return image, image_hash
    except:
        return '', ''


def search_image(data):
    try:
        # 返回和参数key对应的所有值，作为一个Python list返回。
        # 如果key不存在，则返回空list。 It's guaranteed to return a list of some sort..
        images = data.getlist('images')
    except:
        images = data['images']
    pre_start_time = time.time()
    banlist = Reds.smembers('banlist')  # Redis Smembers 命令返回集合中的所有的成员。 不存在的集合 key 被视为空集合
    pre_end_time = time.time()
    # json.dumps() 用于将dict类型的数据转成str
    logger.info(json.dumps({f'{data["pid"]}--invoke_total_time:': pre_end_time - pre_start_time}))  # 记录调用的总共时间
    hash_value_list = []
    down_time_list = []
    cal_time_list = []
    similar_rate = {}
    # 遍历传进来的图片url
    for img in images:
        down_start_time = time.time()
        # 下载图片
        image, image_hash = down_and_hash(img)
        down_end_time = time.time()
        rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)  # 左右翻转

        """
        图像翻转
tf.image.flip_up_down：上下翻转
tf.image.flip_left_right：左右翻转
tf.image.transpose_image：对角线翻转
除此之外，TensorFlow还提供了随机翻转的函数，保证了样本的样本的随机性：
tf.image.random_flip_up_down：随机上下翻转图片
tf.image.random_flip_left_right：随机左右翻转图片
        """

        rvs_image_hash = str(imagehash.phash(rvs_image))
        if image_hash in banlist or rvs_image_hash in banlist:
            continue
        hash_value_list.append(image_hash)
        cal_start_time = time.time()
        # 判断如果单个哈希在'imagehash'的key里,找出对应的ID加入字典

        # hexists查看哈希表 key 中，指定的字段是否存在
        if Reds.hexists('imagehash', image_hash) or Reds.hexists('imagehash', rvs_image_hash):
            if Reds.hexists('imagehash', image_hash):
                similar_ids = Reds.hget('imagehash', image_hash)
            else:
                similar_ids = Reds.hget('imagehash', rvs_image_hash)  # hget获取存储在哈希表中指定字段的值。
            similar_ids = set(json.loads(similar_ids))
            rates = {pid: 1 for pid in similar_ids}  # 只能找到字典的key
            similar_ids.add(int(data['pid']))
            similar_ids = list(similar_ids)
            if len(similar_ids) >= 10:
                Reds.hset('duplicate_10', image_hash, img)
            Reds.hset('imagehash', image_hash, json.dumps(similar_ids))
            similar_rate.update(rates)
        else:
            # hset将哈希表 key 中的字段 field 的值设为 value 。
            Reds.hset('imagehash', image_hash, json.dumps([int(data['pid'])]))
        cal_end_time = time.time()
        down_time_list.append(down_end_time - down_start_time)
        cal_time_list.append(cal_end_time - cal_start_time)
    logger.info(
        json.dumps({f'{data["pid"]}--down_total_time:': sum(down_time_list), 'down_time_list:': down_time_list}))
    logger.info(json.dumps({f'{data["pid"]}--cal_total_time:': sum(cal_time_list), 'cal_time_list:': cal_time_list}))
    similar_rate = json.dumps(similar_rate)
    results = {"pid": int(data['pid']), "similar_rate": similar_rate}
    Reds.hset('reverse', data['pid'], json.dumps(hash_value_list))
    logger.info(json.dumps(results))
    return results


def del_pic(pic_list):
    failed_list = []
    for img in pic_list:
        _, image_hash = down_and_hash(img)

        # HGET key field获取存储在哈希表中指定字段的值。
        pids = Reds.hget('imagehash', image_hash)
        if not pids:
            failed_list.append('{0}删除失败'.format(img))
            continue
        pids = json.loads(pids)
        # hdel删除一个或多个哈希表字段
        Reds.hdel('imagehash', image_hash)
        for pid in pids:
            hash_key = json.loads(Reds.hget('reverse', pid))
            try:
                hash_key.remove(image_hash)
            except:
                failed_list.append('{0}删除失败'.format(img))
                continue
            if not hash_key:
                Reds.hdel('reverse', pid)
            else:
                # HSET key field value将哈希表 key 中的字段 field 的值设为 value 。
                Reds.hset('reverse', pid, json.dumps(hash_key))
    if not failed_list:
        return '全部删除成功'
    return failed_list


def search_pic(imgs):
    data = {}
    banlist = Reds.smembers('banlist')  # Redis Smembers 命令返回集合中的所有的成员。 不存在的集合 key 被视为空集合
    for img in imgs:
        if img.startswith('http://') or img.startswith('https://'):
            _, image_hash = down_and_hash(img)
        else:
            image_hash = img
        if image_hash in banlist:
            data[img] = []
        else:
            # HGET key field获取存储在哈希表中指定字段的值。
            all_pid = Reds.hget('imagehash', image_hash)
            if all_pid:
                data[img] = json.loads(all_pid)
            else:
                data[img] = []
    return data


def cal_imagehash(img):
    _, image_hash = down_and_hash(img)
    return image_hash


def cal_imagehashs(imgs):
    hashs = {}
    for img in imgs:
        _, image_hash = down_and_hash(img)
        hashs[img] = image_hash
    return hashs


def view_banlist():
    banlist = list(Reds.smembers('banlist'))
    return banlist


def add_to_banlist(img_list):
    status_list = []
    for img in img_list:
        dic = dict()
        image, image_hash = down_and_hash(img)
        rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        rvs_image_hash = str(imagehash.phash(rvs_image))
        status1 = Reds.sadd('banlist', image_hash)
        status2 = Reds.sadd('banlist', rvs_image_hash)
        # hdel删除一个或多个哈希表字段
        Reds.hdel('duplicate_10', image_hash)
        Reds.hdel('duplicate_10', rvs_image_hash)
        result = [
            {'hash': image_hash, 'status': status1},
            {'hash': rvs_image_hash, 'status': status2}
        ]
        dic['url'] = img
        dic['result'] = result
        status_list.append(dic)
    return status_list


def del_from_banlist(img_list):
    status_list = []
    for img in img_list:
        _, image_hash = down_and_hash(img)
        # Redis Srem 命令用于移除集合中的一个或多个成员元素，不存在的成员元素会被忽略
        status = Reds.srem('banlist', image_hash)
        status_list.append('{0}的解除黑名单结果:{1}'.format(img, status))
    return status_list


def query_dup_gt_num(pk=10):
    d = dict()
    banlist = list(Reds.smembers('banlist'))
    # Redis Hgetall 命令用于返回哈希表中，所有的字段和值。
    data = Reds.hgetall('imagehash')
    for k, v in data.items():
        # json.loads()用于将str类型的数据转成dict。
        v = json.loads(v)
        try:
            if len(v) >= int(pk) and k not in banlist:
                d.update({k: v})  # Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
        except:
            continue
    return d


def query_dup(datas):
    ha = datas.get('hash')
    try:
        data = datas.getlist('image')
    except:
        data = datas.get('image')
    for i in data:
        try:
            images = data.getlist(i)
        except:
            images = data.get(i)
        # 遍历传进来的图片url
        for img in images:
            # 下载图片
            image, image_hash = down_and_hash(img)
            rvs_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            rvs_image_hash = str(imagehash.phash(rvs_image))
            if str(ha) == image_hash or str(ha) == rvs_image_hash:
                return {ha: img}
    return {ha: None}


def query_all_duplicate():
    d = Reds.hgetall('duplicate_10')
    if not isinstance(d, dict):
        d = json.loads(d)
    data = []
    for i in d:  # i为字典d的key
        data.append({'hash': i, 'image': d[i], 'ids': json.loads(Reds.hget('imagehash', i))})
    return data


if __name__ == '__main__':
    # x = '{"hash":"bf27b039c0a17e86","image":{"373":["http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/8634ee8f44a4780588272c961b4293a1.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/9dc727dac019c332b8f62820c9293a68.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/b9d8c103c32cd42b3e941d858aa2b4ea.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/eb3cd5ee87b086f6793e29c2bf597dcc.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/3beed60529480884ce05f23ca4382fa9.jpg"],"445":["http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/84fa84389d098fefdbc20efe8b2f3a74.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/e428112f5899a98f3428e9b480ace45e.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/828cf9bcc4bd4c1b2b29945cd3b8767b.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/499440483a97b00efdf488374c33c415.jpg","http:\/\/pr.oss-cn-hongkong.aliyuncs.com\/18\/05\/29\/68051729a8db96403ee0759e2b4d5404.jpg"]}}'
    # a = json.loads(x)['image']
    # for j in a:
    #     for i in a[j]:
    #         image, image_hash = down_and_hash(i)
    #         rvs_image = image.transpose(ImagePY.FLIP_LEFT_RIGHT)
    #         rvs_image_hash = str(imagehash.phash(rvs_image))
    #         print(image_hash, rvs_image_hash)
    pic = "http://xxxxx.com/19/04/15/1e91ebbe207aaf1f3752f34afd3141a3.jpg"
    # image, image_hash = down_and_hash(pic)
    # rvs_image = image.transpose(ImagePY.FLIP_LEFT_RIGHT)
    # rvs_image_hash = str(imagehash.phash(rvs_image))
    # print(image_hash, rvs_image_hash)
