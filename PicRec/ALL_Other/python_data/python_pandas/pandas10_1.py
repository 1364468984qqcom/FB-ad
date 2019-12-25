# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

s1 = Series(np.arange(5), index=list('abcde'))
print(s1)
print()
print()
s2 = Series([4, 33, -43, -2313, 434, 44444,34], index=['a', 'b', 'c', 'd', 'e', 'f','h'])
print(s2)
print()
print()
print()
"""
加法
"""
s3 = s1+s2
print(s3)
print()
print()
print()
"""
减法
"""
s4 = s1-s2
print('s4',s4)
print()
print()
print()
"""
乘法：
"""
s5 = s1*s2
print('s5:',s5)
print()
print()
"""
除法：
"""
s6 = s1/s2
print('s6:',s6)