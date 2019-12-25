# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""
numpy.random的使用
"""
n1 = np.random.seed(10)
print('n1', n1)
n2 = np.random.rand(8)  # 在0-1均匀分布的随机样本
print('n2:', n2)
print()
print()
print()
n3 = np.random.randn(3, 4)  # 以给定的形状创建一个数组，数组元素来符合标准正态分布N
print('n3', n3)
print()
print()
print()
print()

"""
Series排序
"""
s1 = Series(np.random.randn(10))
print(s1)
print('排序：')
print(s1.sort_values(ascending=True))
print(s1.sort_index(ascending=True))
print()
print()
print('降序：')
print(s1.sort_index(ascending=False))
print(s1.sort_values(ascending=False))
print()
print()
print()
"""
DataFrame进行排序处理
"""
data = {'a': {'name': 1, 'sex': 2, 'age': 3}, 'b': {'name': 11, 'sex': 22, 'age': 33},
        'c': {'name': 111, 'sex': 222, 'age': 333}, 'd': {'name': 1111, 'sex': 2222, 'age': 3333}}
df1 = DataFrame(data)
print('df1:', df1)
print(df1.describe())
print()
print('对列进行降序排序：', df1.sort_values('a', ascending=False))
print()
print()
print()
print()
df2 = DataFrame(np.arange(15).reshape(5, 3), columns=['A', 'B', 'C'])
print('df2:', df2)
