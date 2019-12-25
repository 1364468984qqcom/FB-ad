# -*- coding: utf-8 -*-
from redis import StrictRedis
import redis

# 字符串  mset批量操作
pool = redis.ConnectionPool(host='localhost', port=6379, password='123456', db=3)
red = StrictRedis(host='localhost', port=6379, db=5, password='123456')
red.mset(name1='张金灿', name2='肖琼')
redPool = redis.Redis(connection_pool=pool)
# 批量操作hash
redPool.hmset('priceHash', {'name1': '张金灿', 'sex1': '1212', 'age1': 2132})
