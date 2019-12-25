# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""
DataFrame对索引或者列进行重命名处理
"""
df1 = DataFrame(np.arange(12).reshape(3, 4), index=['A', 'B', 'C'], columns=['a', 'b', 'c', 'd'])
print('df1:', df1)
df1.index = df1.index.map(str.upper)
print(df1)
print()
print()
print()
df2 = DataFrame({'a': [3, 4, 5, 6], 'b': [33, 44, 55, 66]}, index=['A', 'B', 'C', 'D'])
print(df2)
