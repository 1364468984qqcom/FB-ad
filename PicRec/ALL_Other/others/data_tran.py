import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('ABCD'))
print(df1)
# df2 = df1.T
df1['A'] = [1, 5, 9]
df2 = df1.T
print(df2)
print()
print(df2.duplicated())
print()
print(df2.drop_duplicates())
print()
print(df2.replace(11, np.NAN))
print(df2.replace([3, 10], np.NAN))
print(df2.replace({3: 1111, 7: np.NAN}))
print(df2.replace([3, 10], [np.NAN, 33333]))
print(df2.dtypes)
print(df2.astype(float))
# print(df2.pivot(index='b', values='a', columns='c'))
rolling_sum = df2.rolling(4).min()
print(rolling_sum)
print()
print()
print()
df5 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('ABCD'))
for ix, row in df5.iterrows():
    print(ix)
    print(row)
print()
print()
print()
for ix, col in df5.iteritems():
    print(ix)
    print(col)

dict1 = {'A': {'a': 1, 'b': 2, 'c': 3}, 'B': {'a': 4, 'b': 6, 'c': 8}, 'C': {'a': 11, 'b': -45, 'c': 33},
         'D': {'a': 4, 'b': 6, 'c': 8}}
df6 = pd.DataFrame(dict1)
print(df6)
df7 = df6.T
print(df7)
