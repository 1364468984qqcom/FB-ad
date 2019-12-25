# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_excel('./df1.xlsx')
sns.violinplot(df1['C'], df1['D'])
sns.despine()
plt.show()
