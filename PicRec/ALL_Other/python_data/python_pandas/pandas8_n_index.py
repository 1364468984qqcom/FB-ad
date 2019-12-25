# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

s1 = Series(np.random.randn(6), index=[[1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f']])
print(s1)
print(type(s1))  # <class 'pandas.core.series.Series'>
print()
print(s1[1])
print('类型：', type(s1[1]))  # <class 'pandas.core.series.Series'>

