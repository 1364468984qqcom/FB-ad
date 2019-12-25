# -*- coding: utf-8 -*-
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def tick():
    print('当地时间：{}'.format(datetime.now()))


if __name__ == '__main__':
    schedule = BlockingScheduler()
    schedule.add_job(tick, 'interval', minutes=1)
    print('打印{} to Exit'.format('Break' if os.name == 'nt' else 'C  '))
    try:
        schedule.start()
    # except (KeyboardInterrupt, SystemExit)
    except (KeyboardInterrupt, SystemExit):
        pass
