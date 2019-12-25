# -*- coding: utf-8 -*-

import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('                         当地时间：{}'.format(datetime.now()))


if __name__ == '__main__':
    schedule = BlockingScheduler()
    schedule.add_job(tick, 'cron', hour='16-18', minute='0-59')
    print('打印 {} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        schedule.start()
    except (KeyboardInterrupt, SystemExit):
        pass
