import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

dict1 = {'A': list('123'), 'B': [33, 3342, -4345], 'C': [3.4, 4.5, 66], 'D': [34, 44, 21312]}
df1 = pd.DataFrame(dict1, index=list('abc'))
print(df1)
"""
饼图
"""
# plt.pie(df1['A'].value_counts(normalize=True),labels=df1['A'].value_counts().index,autopct='%1.1f%%',colors=sns.color_palette('Reds'))
# plt.show()

"""
折线图
"""
d = df1.groupby('B').mean()
sns.pointplot(d.index, d['C'])
plt.show()
