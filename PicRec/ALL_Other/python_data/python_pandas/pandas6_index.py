# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1 = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

print(s1)
print()
s2 = s1.reindex(index=['a', 'b', 'c', 'd', 'e', 'f'], fill_value=110)
print(s2)
# s3 = s1.reindex(index=str(range(10)),method='ffill')
# print(s3)