# -*- coding: utf-8 -*-
import schedule
import time


def schedule1():
    print('定时任务')
    print(time.time())


schedule.every(10).seconds.do(schedule1)
while 1:
    schedule.run_pending()
    # time.sleep(.1)
