# -*- coding: utf-8 -*-

from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")
my_db = my_client['pu_get']
my_col = my_db['pu_get1']
# print(my_col)

# a = [
#     {'ti':'1','dest':'zzzzz','u':'wwww'},
#     {'ti':2121,"dest":"2132",'u':'adsdas'},
#     {'ti':'2132','dest':'21312','u':21312}
# ]
#
# c = my_col.insert_many(a)
# print(c.inserted_ids)
#
# b = {'ti':21323,'dest':'wqd','u':'2313'}
# x = my_col.insert_one(b)
# print(x.inserted_id)

# for a in my_col.find():
#     print(a)

data = my_col.find({'ti':"1"})
for i in data:
    print(i)