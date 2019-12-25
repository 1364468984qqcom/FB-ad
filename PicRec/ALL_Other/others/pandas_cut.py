import pandas as pd
import numpy as np

"""
pandas分箱技术
"""
s1 = pd.Series(np.random.randint(20, 100, size=30))
print(type(s1))
print(s1)
bins = [0, 59, 70, 80, 100]
print()
sorce_num = pd.cut(s1, bins, labels=['bad', 'normal', 'good', 'great'])
print('hhhhhh:', sorce_num)
print()
sorce_count = pd.value_counts(sorce_num)
print(sorce_count)
print()
print()
print()
df1 = pd.DataFrame()
print(type(df1))
df1['sorce'] = s1
# print(df1)
df1['student'] = [pd.util.testing.rands(4) for i in range(30)]  # 可以生成30个随机4位字符串
# print(df1)
categories = pd.cut(df1['sorce'], bins, labels=['pie', 'yi_ban', 'hao', 'hen_hao'])
df1['categories'] = categories
# print(df1)
count = pd.value_counts(categories)
print(count)
print(df1)
print()
print(df1.ix[6])
print()
print(df1.loc[6:9])

print()
print()
print()

seq = ("raaa", "uaaa", "naa", "aao", "oaa", "baa")  # 字符串序列
print(','.join(seq))
print(''.join(seq))
print(type(','.join(seq)))
