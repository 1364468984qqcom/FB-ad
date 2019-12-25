# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df1 = pd.read_excel('./df1.xlsx')
print(df1)
fig = plt.figure()
plt.title('BOXPLOT')
plt.xlabel('X')
plt.ylabel('Y')
ax = fig.add_subplot(2, 1, 1)
ax.boxplot(df1['A'])
plt.show()
