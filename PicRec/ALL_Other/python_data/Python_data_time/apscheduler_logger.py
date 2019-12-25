# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime
import logging
from python_data.Python_data_time.smtp_lib_mail3 import mail

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', filename='log1.txt', filemode='a')


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def date_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %D:%M:%S'), x)
    print(1 / 0)


def my_listener(event):
    if event.exception:
        print('任务出错了！')
        mail()

        # return
    else:
        print('任务照常运行')


scheduler = BlockingScheduler()
scheduler.add_job(func=date_test, args=('一次性任务，会出错!',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')
scheduler.add_job(func=aps_test, args=('循环练习',), trigger='interval', seconds=3, id='interval_task')
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler._logger = logging
scheduler.start()
