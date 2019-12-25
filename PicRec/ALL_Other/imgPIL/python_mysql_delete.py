# -*- coding: utf-8 -*-

from pymysql import connect

db = connect(host='localhost', user='root', password='123456', db='eleloves', port=3306,charset='utf8')
cursor = db.cursor()

# delete_sql = """delete from table1 where id =1"""

# try:
#     cursor.execute(delete_sql)
#     db.commit()
# except:
#     pass
# finally:
#     db.close()

insert_sql = """insert into table1 (id,name,sex,age) values (1,'张金灿','男','18')"""
try:
    cursor.execute(insert_sql)
    db.commit()
except Exception as d:
    print(d)
finally:
    db.close()
