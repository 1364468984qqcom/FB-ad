# -*- coding: utf-8 -*-

from pymysql import connect

db = connect(host='localhost', user='root', password='123456', db='eleloves', port=3306)
cursor = db.cursor()

sql = """ update table1 set age = 888888888 where id =2"""
try:
    cursor.execute(sql)
    db.commit()
except:
    pass
finally:
    db.close()
