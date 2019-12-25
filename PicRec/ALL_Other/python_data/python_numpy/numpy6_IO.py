# -*- coding: utf-8 -*-

import numpy as np

array1 = np.array([[[1, 2, 3], [2, 3, 4]], [[4, 5, 6], [5, 6, 7]], [[2, 6, 9], [3, 6, 0]]])
print(array1)
print()
np.save('numpy.npy', array1)
np.save('numpy2', array1)
print()
print()
print()
array2 = np.load('numpy2.npy')
print(array2)
print()
print()
print()

print(array2.shape)
