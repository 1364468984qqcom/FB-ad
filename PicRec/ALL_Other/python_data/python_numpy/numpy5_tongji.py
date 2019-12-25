# -*- coding: utf-8 -*-
import numpy as np

array1 = np.array([[13, 411, 185], [226, 7, 88888888], [111, 22, 39]])
array2 = np.array([[[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [55, 66, 777777777]], [[44, 22, 11], [66, -9, 0]]])

print(array1)
print()
print(array2)
print()
print('array1_amin:', np.amin(array1))
print()
print('array2_amin:', np.amin(array2))
print()
print('array1_amax:', np.amax(array1))
print()
print('array2_amax:', np.amax(array2))
print()
print()
print()
print()
print('a1:', np.amin(array1, 0))  # a1: [13  2 39]
print()
print('a2:', np.amin(array1, 1))  # a2: [4 7 2]
