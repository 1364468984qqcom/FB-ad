# -*- coding: utf-8 -*-

import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
pu_get = myClient['puget']
my_col = pu_get['puget']
# print(my_col)

data_list = [
    {'title': "中国石油", 'des': "游戏公司", "url": "www.baidu.com"},
    {'title': '中国石化', "des": "异乡故事粤语", 'url': "www"},
    {'title': "图像处理", 'des': "图像处理/图像识别", 'url': 'www'},
    {'title': '机器学习', 'des': '机器学习的体验', "url": "wwwwwww"}
]

a = my_col.insert_many(data_list)
print(a.inserted_ids)

# import pymongo
#
# uri = "mongodb://"+ 'root'+':'+'123456'+"@"+"localhost"+":"+"27017"+"/"+"puget"
# myClient = pymongo.MongoClient(uri)
# myClient.admin.authenticate('root','123456')
# pu_get = myClient['puget']
# my_col = pu_get['puget']
# # print(my_col)
#
# data_list = [
#     {'title': "中国石油", 'des': "游戏公司", "url": "www.baidu.com"},
#     {'title': '中国石化', "des": "异乡故事粤语", 'url': "www"},
#     {'title': "图像处理", 'des': "图像处理/图像识别", 'url': 'www'},
#     {'title': '机器学习', 'des': '机器学习的体验', "url": "wwwwwww"}
# ]
#
# a = my_col.insert_many(data_list)
# print(a.inserted_ids)
