# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""
map的操作
"""
df1 = DataFrame({'城市': ['上海', '北京', '成都', '福州', '深圳'], '入口': ['1000', '2000', '3000', '4000', '5000']})
print(df1)
print()
print()
# 使用eries添加一列
df1['GDP'] = Series([12345, 25485, 445454, 58475, 56555])
print(df1)
print()
print()
# 使用map添加一列
gdp_map = {'上海': 121212, '北京': 4545747, '成都': 421521, '福州': 5427454, '深圳': 2141212}
df1['GDP1'] = df1['城市'].map(gdp_map)
print(df1)
print()
print()
# 修改索引
# df1.reindex(index=['a', 'b', 'c', 'd', 'e'])

print()
print()
df1.index = ['A', 'B', 'C', 'D', 'E']
print(df1)
print()
print()
print()
# Series 修改的话，必须添加索引  # 需要修改索引，map则不用
df1['天气'] = Series(['多云', '小雨', '大雨', '威风', '海风'], index=['A', 'B', 'C', 'D', 'E'])
print(df1)
