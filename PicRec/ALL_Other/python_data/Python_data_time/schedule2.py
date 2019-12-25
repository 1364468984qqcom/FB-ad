# -*- coding: utf-8 -*-
import schedule
import time

print(time.time())


def schedule_2():
    print('定时任务')


schedule.every().hour.do(schedule_2)

while 1:
    schedule.run_pending()
