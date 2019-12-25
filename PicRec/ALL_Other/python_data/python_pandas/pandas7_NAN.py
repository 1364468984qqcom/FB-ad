# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

nan = np.nan
print(type(nan))  # <class 'float'>
print()
s1 = Series([1, 2, np.nan, 3, 4], index=['a', 'c', 'v', 'b', 'd'])
print(s1)
print()
null = s1.isnull()
print(null)
print()
print()
print('notnull:', s1.notnull())
print()
"""
去掉NAN的值
"""

print('去掉NAN的值：', s1.dropna())
print()
print()
print()

"""
DataFrame中使用NAN
"""

df = DataFrame([[1, 2, np.nan, np.nan], [4, 5, np.nan], [55, 66, np.nan]])
print(df)
print(df.isnull())
print()
print()
print()
print()
print('行：',df.dropna(axis=0))
print(df.dropna(axis=1))