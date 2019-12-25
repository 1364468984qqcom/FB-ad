# -*- coding: utf-8 -*-
import schedule
import time

print(time.time())


def schedule_3():
    print('定时任务')


# schedule.every().day.do(schedule_3)
#
# while 1:
#     schedule.run_pending()
#
#
schedule.every().day.at("10:00").do(schedule_3)