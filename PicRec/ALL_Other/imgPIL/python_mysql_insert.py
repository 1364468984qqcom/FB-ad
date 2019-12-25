# -*- coding: utf-8 -*-

from pymysql import connect

db = connect(host='localhost', user='root', password='123456', db='eleloves', port=3306, charset='utf8')

cur = db.cursor()

insert_sql = """insert into table1(id,name,sex,age) values (7,"zjc",'girl',225)"""

try:
    cur.execute(insert_sql)
    db.commit()

except:
    pass
db.close()
