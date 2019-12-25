# -*- coding: utf-8 -*-

import time

ticks = time.time()
print('时间戳：', ticks)
print()
localTime = time.localtime(time.time())
print('当地时间：', localTime)
print()
localTime2 = time.asctime(time.localtime(time.time()))
print('真正的当地时间：', localTime2)
strTime = time.strftime("%Y/%m/%d %H:%M:%S")
print('格式化时间为：',strTime)