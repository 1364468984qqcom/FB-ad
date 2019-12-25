# -*- coding: utf-8 -*-

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('./df1.xlsx')
var = df1.groupby(['C']).sum().stack()
temp = var.unstack()

print(type(temp))
x_list = temp['A']
label_list = temp.index
plt.axis('equal')
plt.pie(x_list, labels=label_list, autopct='%1.1f%%')
plt.title('bing_tu')
plt.show()

ax1 = plt.gca()
ax2 = plt.gcf()