# -*- coding: utf-8 -*-
import numpy as np

# numpy.empty
array1 = np.empty([3, 4], dtype=int)
print(array1)
print(array1.shape)
print(array1.ndim)
print()
# array 创建数组
array2 = np.array([[3, 4, 5, 8], [4, 534, 53453, 21], [31, 13, 32, 1232]])
print(type(array2))
print('array2', array2)
print(array2.shape)
print(array2.ndim)
print()

# numpy.zeros
array3 = np.zeros((3, 5), dtype=np.int)
print('array3', array3)
print(array3.shape)
print(array3.ndim)

print()

# 三维数组
array4 = np.array(
    [[[3, 42, 4], [32, 43, 1], [4, 6, 3]], [[34, 2, 1], [4, 5, 7], [5, 6, 7]], [[3, 42, 4], [423, 43, 4], [4, 7, 6]]])
print('array4:', array4)
print(array4.shape)
print(array4.ndim)
print()

array5 = np.zeros((3, 5, 3))
print('array5', array5)
print(array5.shape)
print(array5.ndim)
print(array5.size)
print(array5.itemsize)
print(array5.flags)
print(array5.real)
print()
print()
print()
print(array5.imag)
print(array5.data)
# reshape
print()
a = array5.reshape(3, 5, 3)
print(a)
print()
