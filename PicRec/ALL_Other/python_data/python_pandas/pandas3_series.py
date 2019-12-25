# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

"""
Series 是一个带有 名称 和索引的一维数组，
既然是数组，肯定要说到的就是数组中的元素类型，
在 Series 中包含的数据类型可以是整数、浮点、字符串、Python对象等
"""
s1 = pd.Series([2, 3, 4, 'aaa', 6])
print(s1)
print()
print(type(s1))
print(s1.size)
print(s1.ndim)
print(s1.shape)
print(s1.values)
print()
print('index:', s1.index)
print()
print()
print()
"""
使用数组创建
"""
s2 = pd.Series(np.arange(4, 10))
print(s2)
print()
print()
print()
s2_1 = pd.Series(np.array([45, 66, 5]))
print('s2-1', s2_1)

"""
使用字典创建
"""

s3 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(s3)
print()
print()
s4 = pd.Series([3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f'], dtype=np.int64)
print(s4)
print(s4.values)
print(s4.shape)
print('d:')
print(s4['d'])

print()
print()
print()
print(s4[s4 > 5])  # 打印实际上大于5的元素
print(s4[s4[0] > 5])  # 打印他的数量
print()
print()
print()
dict1 = s4.to_dict()  # Series 转化为字典
print(dict1)
