# -*- coding: utf-8 -*-

from pymysql import connect

db = connect(host='localhost', user='root', password='123456', db='eleloves', port=3306, charset='utf8')

sercur = db.cursor()

sql = 'select * from table1'
try:
    sercur.execute(sql)
    result = sercur.fetchall()
    for row in result:
        id = row[0]
        name1 = row[1]
        sex = row[2]
        age1 = row[3]
        print('id:', id, 'name:', name1, 'sex:', sex, 'age:', age1)
except Exception as w:
    pass
finally:
    db.close()
