# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

"""
使用Series操作Replace
"""
s1 = Series(np.arange(10, 40, 2))
print(s1)
print()
print()
# 替换replace
s2 = s1.replace(2, np.nan)
print(s2)

"""
替换多个值
"""

s1.replace([2, 4, 12], [np.nan, np.nan, np.nan])
print(s1)
