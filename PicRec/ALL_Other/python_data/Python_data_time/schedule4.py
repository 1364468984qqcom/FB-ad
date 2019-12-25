# -*- coding: utf-8 -*-
import schedule
import time


def schedule_5(reu):
    print('定时任务:{}'.format(reu))


schedule.every().day.at("9:30").do(schedule_5, 10)

while 1:
    schedule.run_pending()
