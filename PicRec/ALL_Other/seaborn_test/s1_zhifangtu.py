# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import current
import numpy as np

# df1 = pd.DataFrame(np.arange(60).reshape(10, 6), index=list('abcdefghij'), columns=list('ABCDEF'))
# df1.to_excel('df1.xlsx')
# df1 = pd.read_excel('./df1.xlsx')
df1 = pd.DataFrame(np.array([[3, 4, 5], [.3, .333, -.35], [-55, 54, 234]]))
print(df1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df1[1], bins=11)
plt.title('直方图')
plt.xlabel('ABC')
plt.ylabel('abc')
plt.show()
