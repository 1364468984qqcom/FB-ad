import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.DataFrame(np.arange(20).reshape(4, 5), index=list('abcd'), columns=['BJ', 'CD', 'SZ', 'SH', 'GZ'])
# df1['CD']['b'] = 11
# df1['CD']['d'] = 1
# print(df1)
# group_ = df1.groupby(df1['CD'])
# print(group_)
# cd_1 = group_.get_group(1)
# print(cd_1.mean())
# print()
# print(group_.agg('min'))
print(df1)
print(tuple(list(df1['BJ'])))
print(df1['BJ'].to_list())

if 10 in list(df1['BJ']):
    print(5)
else:
    print(8)

if sum(list(df1['BJ'])) > 190:
    print(5)
else:
    print(8)
