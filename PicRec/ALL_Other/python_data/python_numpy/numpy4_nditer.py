# -*- coding: utf-8 -*-


import numpy as np

array1 = np.arange(3, 26, 2).reshape(4, 3)
print(array1)
print()
array2 = array1.T
print(array2)
print()
print()
for i in np.nditer(array1):
    print(i, end=', ')

print()
for a in np.nditer(array1.T.copy(order='C')):
    print(a, end=', ')
print()
for b in np.nditer(array1.T.copy(order='F')):
    print(b, end=', ')
