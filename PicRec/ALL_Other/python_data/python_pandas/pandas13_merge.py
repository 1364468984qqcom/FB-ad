# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

"""
对两个DataFrame进行merge处理
"""
# print(np.arange(10, 40, 2))
df1 = DataFrame(np.arange(10, 50, 2).reshape(4, 5), columns=['A', 'B', 'C', 'D', 'E'], index=['a', 'b', 'c', 'd'])
print('df1:')
print(df1)
# print(np.arange(400, 800, 20))
df2 = DataFrame(np.arange(400, 800, 20).reshape(4, 5), columns=['A', 'B', 'C', 'D', 'E'], index=['a', 'b', 'c', 'd'])
print(df2)
print('合并：')
df3 = pd.merge(df2,df1)
print(df3)