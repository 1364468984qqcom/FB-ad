# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

ser1 = pd.Series(np.arange(6), index=['a', 'b', 'c', 'd', 'e', 'f'])
print(ser1)
ser2 = pd.Series(np.random.randn(4), index=[1, 2, 3, 4])
print(ser2)
