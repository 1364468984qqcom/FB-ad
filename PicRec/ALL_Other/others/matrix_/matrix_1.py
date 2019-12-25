# import numpy as np
#
# mylist = [[1, 2, 3], [4, 5, 6]]  # 列表
# print(type(mylist))
# print(mylist, end='\n\n')
#
# myarray = np.array(mylist)  # 列表转数组
# print(type(myarray))
# print(myarray, end="\n\n")
#
# mymatrix = np.mat(mylist)  # 列表转矩阵
# print(type(mymatrix))
# print(mymatrix, end='\n\n')
#
# MatToArray = np.array(mymatrix)  # 矩阵转数组
# print(type(MatToArray))
# print(MatToArray, end='\n\n')
#
# ArrayToMat = np.mat(myarray)  # 数组转矩阵
# print(type(ArrayToMat))
# print(ArrayToMat, end='\n\n')
#
# MatToList1 = mymatrix.tolist()  # 矩阵转列表
# print(type(MatToList1))
# print(MatToList1)
# MatToList2 = list(mymatrix)  # 注意点1
# print(type(MatToList2))
# print(MatToList2, end='\n\n')
#
# ArrayToList1 = myarray.tolist()  # 矩阵转列表
# print(type(ArrayToList1))
# print(ArrayToList1)
# ArrayToList2 = list(myarray)  # 注意点2
# print(type(ArrayToList2))
# print(ArrayToList2)


import numpy as np

array = np.arange(12).reshape(3, 4)
array_to_matrix = np.mat(array)
print(array_to_matrix)
print(type(array_to_matrix))
print()
list1 = [3, 4, 5, 7, 8]
list_to_matrix = np.mat(list1)
print(list_to_matrix)
print(type(list_to_matrix))
print()
list2 = [[4, 56, 7, 8], [99999, 9, 9, 9]]
print(type(list2))
list2_to_matrix = np.mat(list2)
print(list2_to_matrix)
print(type(list2_to_matrix))
print()
print()
matrix_to_array = list2_to_matrix.A
print(matrix_to_array)
print(type(matrix_to_array))
