# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel('./df1.xlsx').groupby('A').apply(lambda x:x.C).unstack().T.plot.box()
print(df1)

df2 = pd.DataFrame(np.arange(12).reshape(4, 3), index=list('abcd'), columns=list('ABC'))
D = df2.groupby('A').apply(lambda s: s.B).unstack().T.plot.box()
print(D)

f = df2.boxplot(column='C',by='A')
d = df2.histplot(column='A',by='C')
print(d)
print(f)