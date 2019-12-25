import pandas as pd
import numpy as np

s1 = pd.Series([2, 3, 5, 7, 89, 2, 3])
print(type(s1))
print(s1.dtype)
# print(s1.unstack())

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
print(df1)
print(df2)
print()
print(pd.merge(df2, df1))
print(df2.merge(df1))