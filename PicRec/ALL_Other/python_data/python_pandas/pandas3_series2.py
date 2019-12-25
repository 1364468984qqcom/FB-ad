# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

index_1 = ['a', 'b', 'c', 'd', 'e']
s5 = pd.Series({'a':3, 'b':4, 'c':5, 'd':9})
s6 = pd.Series(s5, index=index_1)
print(s6)
print(s6.isnull)
print(pd.isnull(s6))
print(pd.notnull(s6))
s6.name = 'zjc'
print(s6.name)
print(s6)