# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser

# link = 'http://www.tiobe.com/tiobe-index/'
# print(webbrowser.open(link))
# print()
# print()
# print()
# df = pd.read_clipboard()
# print(df)

df1 = pd.DataFrame({'a': [4, 5, 6, 7], 'b': [7, 4, 6, 8]})
print(df1)
print()
print(type(df1))
print(df1.values)
print()
print(type(df1.values))  # <class 'numpy.ndarray'>
print(df1.size)
print()
print(df1.shape)
print(df1.values.itemsize)
print(df1.values.size)
print(df1.values.ndim)
print(df1.ndim)

"""
使用嵌套字典创建DataFrame
"""
df2 = pd.DataFrame({'a': {'name': 'zjc', 'age': '11', }, 'b': {'name': 'zjc1', 'age': '111', 'sex': 'nan1'},
                    'c': {'name': 'zjc2', 'age': '112', 'sex': 'nan2'}})
print(df2)
print()
print()
"""
使用Series创建DataFrame
"""
df3 = DataFrame(
    {'a': Series([1, '2', 3]), 'b': Series([3, 4, 5]), 'c': Series([44, 55, 66]), 'd': Series([55, 66, 222])})
print(df3)
print()
print()
print(df3.values.itemsize)  # 字节大小
print(df3.ndim)
print(df3.values)
print()
print()
print()
array1 = np.array([[3, 'aa', 44], [55, 6, 6], ['ddd', 'ccc', 35]])
print(array1)
