# -*- coding: utf-8 -*-
import schedule
import pymysql
import time
import random

sql_list = [
    """insert into test (id,name, sex, age) values ('1','zjc','boy','15')""",
    """insert into test (id,name, sex, age) values ('1','zjc','boy','15')""",
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
    print(n)
    cursor.execute(sql_insert)
    conn.commit()
    conn.close()


print('执行前时间为：', time.time())

# schedule.every().minute.do(insert)
schedule.every(2).seconds.do(insert)
while 1:
    schedule.run_pending()
# print('执行完成时间：', time.time())
