"""
2019.9.17
执行将redis的图像识别的db5下面的imagehash的数据导出
"""

import redis
import json


redis = redis.StrictRedis(host='pc-j6cf399s8cow1q852.rwlb.rds.aliyuncs.com',  password='SfPXDORZIxF57P78', db=5,
                          decode_responses=True, charset='utf8')
db5 = redis.hgetall('imagehash')

with open('./imagehash.json', 'w', encoding='utf-8') as file:
    db5 = json.dumps(dict(db5))
    file.write(db5)

"""
2019.9.17
执行将redis的图像处理的db5下面的reverse的数据导出
"""
import redis
import json

redis = redis.StrictRedis(host='r-j6cvndklhoxkmtv3vl.redis.rds.aliyuncs.com', password='sITfOURxCSaqT4Sa4E', db=5,
                          decode_responses=True, charset='utf8')
db5 = redis.hgetall('reverse')
print(db5)
print()
with open('./reverse.json', 'w', encoding='utf-8') as file:
    db5 = json.dumps(dict(db5))
    file.write(db5)
