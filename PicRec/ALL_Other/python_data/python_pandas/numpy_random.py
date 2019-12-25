# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import mat

array = np.random.rand(4,3)
print(array)
print(type(array))
max_t = mat(array)
print(max_t)
print(type(max_t))
print()
print()
print()
mat1 = np.mat([[3,4,5],[6,7,8],[9.0,22,33]])
print(mat1)
print(type(mat1))
print()
print()
print()
array = mat1.A
print(array)
print(type(array))
list2 = mat1.tolist()
print(type(list2))
str1 = mat1.tostring()
print(type(str1))