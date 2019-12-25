# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_excel('./df1.xlsx')
var = df1.groupby('C').Sales.sum()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('C')
ax.set_ylabel('CC')
ax.set_title('CCCCCCCCCC')
var.plot(kind='line')
plt.show()
