# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import openpyxl, xlsx

# import tables

data = {'a': {'name': 'zjc1', 'sex': '男1', 'age': 20}, 'b': {'name': 'zjc2', 'sex': '男2', 'age': 22},
        'c': {'name': 'zjc3', 'sex': '男3', 'age': 222}, 'd': {'name': 'zjc4', 'sex': '男4', 'age': 120}}

df1 = DataFrame(data)
# df1.to_csv('data1.csv')
# df1.to_excel('data1.xlsx')
# dict1 = df1.to_dict()  # DF转为字典
# df1_1 = DataFrame(dict1)  # 将字典转为DF
# print(df1_1)
# print(dict1)
# df1.to_json('data.json')
# df1.to_hdf('data.h5', 'df1')
# df1.to_html('data1.html')
df2 = pd.read_csv('D:\WorkProject\ImageProject\PicRec\python_data\python_pandas\data1.csv')
print('df2：', df2)
print()
print('xlrd:', pd.read_excel('data1.xlsx'))
print()
print()
print('json', pd.read_json('data.json'))
print()
print()
print('html:', pd.read_html('data1.html'))
