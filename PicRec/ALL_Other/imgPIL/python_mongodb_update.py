# -*- coding: utf-8 -*-

from pymongo import MongoClient

my_client = MongoClient('mongodb://localhost:27017/')
my_db = my_client['pu_get2']
my_col = my_db['puget2']

data = [
    {'tit': 213, 'des': '21331', 'id': 231312},
    {'tit': '2313', 'des': '21323sdadas', 'id': '23sdasd'},
    {'tit': 'w23213', 'des': 'wdasda', 'id': '3213'}
]
a = my_col.insert_many(data)
# print(a.inserted_ids)
# my_col.insert_many(data)

update_data = {'tit': {"$regex": "^w"}}
new_value = {"$set": {'id': 1111111111}}
s = my_col.update_many(update_data, new_value)
print(s.modified_count)

delete_data = {'tit': 213}
my_col.delete_one(delete_data)

my_col.delete_many({})

my_col.drop()
