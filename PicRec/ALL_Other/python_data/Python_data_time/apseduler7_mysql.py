# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import pymysql
import random

sql_list = [
    """insert into test (id,name, sex, age) values ('1','zjc','boy','15')""",
    """insert into test (id,name, sex, age) values ('10','zjc10','boy10','1510')""",
    """insert into test (id,name, sex, age) values ('2','zjc2','boy2','152')""",
    """insert into test (id,name, sex, age) values ('3','zjc3','boy3','153')""",
    """insert into test (id,name, sex, age) values ('4','zjc4','boy4','154')""",
    """insert into test (id,name, sex, age) values ('5','zjc5','boy5','155')"""
]


def insert():
    conn = pymysql.connect('localhost', 'root', '123456', 'test1')
    cursor = conn.cursor()
    if not cursor:
        print('数据库链接失败')
        raise Exception('我的数据库没有链接哦')
    n = random.randint(0, len(sql_list) - 1)
    sql_insert = sql_list[n]
    print('索引：{}'.format(n))
    print('当地时间：{}'.format(datetime.now()))
    cursor.execute(sql_insert)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    schedule = BlockingScheduler()
    schedule.add_job(insert, 'interval', seconds=1)
    try:
        schedule.start()
    except (KeyboardInterrupt, SystemExit):
        pass
