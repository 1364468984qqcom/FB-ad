# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""
# 透视表：pivot_table
# pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
"""

df = DataFrame({
    '类别': ['水果', '水果', '水果', '蔬菜', '蔬菜', '肉类', '肉类'],
    '产地': ['美国', '中国', '中国', '中国', '新西兰', '新西兰', '美国'],
    '水果': ['苹果', '梨', '草莓', '番茄', '黄瓜', '羊肉', '牛肉'],
    '价格': [5, 5, 10, 3, 3, 13, 20],
    '数量': [5, 5, 9, 3, 2, 10, 8],
})
print(df)
print()
print()
print(type(df))
print(df.shape)
print(df.ndim)
print(df.size)
print()
print()
print()
print('info:', df.info())
print()
print()
print()
print()
print(df.pivot_table(index=['产地', '类别']))
print()
print()
print(df.pivot_table(columns=['产地', '类别']))
print()
print()
print()
"""
交叉表
交叉表是用于统计分组频率的特殊透视表
"""
print('交叉表：')
df1 = DataFrame({
    '类别': ['水果', '水果', '水果', '蔬菜', '蔬菜', '肉类', '肉类'],
    '产地': ['美国', '中国', '中国', '中国', '新西兰', '新西兰', '美国'],
    '水果': ['苹果', '梨', '草莓', '番茄', '黄瓜', '羊肉', '牛肉'],
    '价格': [5, 5, 10, 3, 3, 13, 20],
    '数量': [5, 5, 9, 3, 2, 10, 8],
})

print(pd.crosstab(df1['类别'], df1['产地'], margins=True))  # 按照类别分组，统计各个分组产地的的频数
