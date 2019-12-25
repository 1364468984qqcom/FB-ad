"""
2019.9.17
执行将linux的imagehash数据导入到redis图像识别服务器
"""
import redis
import json

conn = redis.Redis(host='127.0.0.1', port='6379', db=5, password='WFOkSMvtzp4W6ymK')
with open('/data/app/imagehash.json') as file:
    test = json.load(file)
    conn.hmset('imagehash', test)

"""
2019.9.17
执行将linux的reverse数据导入到redis图像识别服务器
完成文件迁移操作
"""
import json
import redis

conn = redis.Redis(host='127.0.0.1', port=6379, db=5, password='WFOkSMvtzp4W6ymK')
with open('/data/app/reverse.json') as file:
    test = json.load(file)
    conn.hmset('reverse', test)
