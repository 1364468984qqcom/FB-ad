# -*- coding: utf-8 -*-
import numpy as np
import numpy.matlib

array1 = np.array([[2, 3, 4], [45, 6, 77], [6, 7, 8]])
array2 = np.array([[33, 44, 55], [55, 66, 77], [88, 99, 11]])

# a3 = np.array([[1, 2, 3], [2, 3, 4]], [[2, 3, 5], [5, 6, 7]])
# a4 = np.array([[3, 6, 5], [33, 44, 55]], [[22, 33, 11], [4, -44, -2]])

"""# numpy.dot()
# numpy.dot() 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；
# 对于二维数组，计算的是两个数组的矩阵乘积；对于多维数组，它的通用计算公式如下，
# 即结果数组中的每个元素都是：数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和"""
dot1 = np.dot(array1, array2)
print('array1 和array2的dot：', dot1)
# dot2 = np.dot(a4, a3)
# print('a3和a4的dot:', dot2)
print()
print()
print()

"""# 求数组的vdot
# numpy.vdot() 函数是两个向量的点积。 如果第一个参数是复数，那么它的共轭复数会用于计算。 如果参数是多维数组，它会被展开。"""
vdot = np.vdot(array2, array1)
# vdot = 3*44+66+4*55+45*55+6*66+77*77+6*88+7*99+8*11
print('array1 和array2的vdot：', vdot)
print()
print()
print()
"""
numpy.inner()
numpy.inner() 函数返回一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积。
"""
a = np.array([[2, 34, 5], [55, 6, 77], [55, 6453, 22], [2131, 32, -41]])
b = np.array([[-312, 12, 3], [-32, -32312, -32], [431, 123, 45], [2, -43, -54]])
print(a)
print()
print(b)
print()
print()
print()
inner = np.inner(a, b)
# inner = [[2 * -312 + 34 * 12 + 5 * 3, 2 * -32 + 34 * -32312 + 5 * -32, 2 * 431 + 34 * 123 + 5 * 45,
#           2 * 2 + 34 * -43 + 5 * -54],
#          [55 * -312 + 6 * 12 + 77 * 3, 55 * -32 + 6 * -32312 + 77 * -32, 55 * 431 + 6 * 123 + 77 * 45,
#           55 * 2 + 6 * -43 + 77 * -54],
#          [55 * -312 + 6453 * 12 + 22 * 3, 55 * -32 + 6453 * -32312 + 22 * -32, 55 * 431 + 6453 * 123 + 22 * 45,
#           55 * 2 + 6453 * -43 + 22 * -54],
#          [2131 * -312 + 32 * 12 + -41 * 3, 2131 * -32 + 32 * -32312 + -41 * -32, 2131 * 431 + 32 * 123 + -41 * 45,
#           2131 * 2 + 32 * -43 + -41 * -54]]
print('a和b的inner为：', inner)
print()
print()
print()
"""
numpy.matmul
numpy.matmul 函数返回两个数组的矩阵乘积。 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播。
另一方面，如果任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除。
对于二维数组，它就是矩阵乘法：
"""

a = np.array([[3, 4], [4, 5]])
b = np.array([[3, 65], [66, 77]])
print(type(a))
matmul = np.matmul(a, b)
print('a和b的matmul为：', matmul)
print()
print()
print()

c = [[[2, 3], [45, 6]], [[33, 3], [5, 6]]]
print(type(c))
print()
asarray = np.asarray(c)
print(type(c))
print()
print()
print()

"""
numpy.linalg.det()
numpy.linalg.det() 函数计算输入矩阵的行列式。
行列式在线性代数中是非常有用的值。 它从方阵的对角元素计算。 对于 2×2 矩阵，它是左上和右下元素的乘积与其他两个的乘积的差。
换句话说，对于矩阵[[a，b]，[c，d]]，行列式计算为 ad-bc。 较大的方阵被认为是 2×2 矩阵的组合。
"""

det_a = np.linalg.det(a)
print(det_a)
det_b = np.linalg.det(b)
print(det_b)
print()
print()
print()
"""
numpy.linalg.solve()
numpy.linalg.solve() 函数给出了矩阵形式的线性方程的解。
考虑以下线性方程：
"""
slove = np.linalg.solve(a, b)
print(slove)
print()
print()
print()
"""
numpy.linalg.inv()
numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵。
逆矩阵（inverse matrix）：设A是数域上的一个n阶矩阵，若在相同数域上存在另一个n阶矩阵B，
使得： AB=BA=E ，则我们称B是A的逆矩阵，而A则被称为可逆矩阵。注：E为单位矩阵。
"""
inv_a = np.linalg.inv(a)
print('inv_a:', inv_a)
inv_b = np.linalg.inv(b)
print('inv_b:', inv_b)

