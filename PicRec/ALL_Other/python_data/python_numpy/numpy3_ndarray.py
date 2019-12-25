# -*- coding: utf-8 -*-

import numpy as np

# 默认为浮点数
x = np.zeros(5)
print(x)
print()

# 设置类型为整数
y = np.zeros((5), dtype=np.int)
print(y)
print()

# # 自定义类型
# z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
# print(z)
# print()
print()
print()
print()
print()
array = np.array([[[3,4,5,6],[3,6,7,4]],[[4,5,6,7],[1,6,7,9]],[[5,9,0,8],[4,8,7,3]]])
print(array.shape)
print(array)
print(array.ndim)
print()
print()
print()

array2 = np.ones([5,2],dtype=int)
print(array2)
print(array.shape)
print(array2.ndim)