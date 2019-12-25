# -*- coding: utf-8 -*-

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, password='123456', db='12')
red = redis.Redis(connection_pool=pool)
# print(red)



