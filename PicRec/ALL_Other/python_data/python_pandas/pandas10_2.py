# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(4).reshape(2, 2), index=['a', 'b'], columns=['BJ', 'GZ'])
print(df1)
print()
print()
df2 = DataFrame(np.arange(20).reshape(5, 4), index=['a', 'b', 'c','e','f'], columns=['BJ', 'GZ', 'SH','SB'])
print(df2)
print()
print()
print()
df3 = df2 + df1
print('df3:')
print(df3)
print()
print()
print()
df4 = df1 - df2
print('df4:')
print(df4)
print()
print()
print()
df5 = df1 * df2
print('df5:')
print(df5)
print()
print()
print()
df6 = df1 / df2
print('df6:')
print(df6)
print()
print()
"""
使用df2为案列
"""
print(df2.sum())
print(df2.max())
print()
print(df2.min())

print()
print()
print(df2)
print()
print(df2.max(axis=1))
print(df2.max())
print()
print()
df2 = DataFrame(np.arange(16).reshape(4, 4), index=['a', 'b', 'c','e'], columns=['BJ', 'GZ', 'SH','SB'])

print(df2.min())
print()
print()
print()
print()
print(df2)
print()
print()
print(df2.describe())

