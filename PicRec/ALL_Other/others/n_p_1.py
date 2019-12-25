import numpy as np
import pandas as pd

n1 = np.arange(12).reshape(3, 4)
print(n1)
# n2 = np.array([[4, 15, 7, 3, ], [5, 26, 7, 8], [6, 7, 18, 9]])
# print(n2)

# n3 = np.add(n1, n2)
# print(n3)
print()
n4 = np.sum(n1, axis=0)
print(n4)
n5 = np.sum(n1, axis=1)
print(n5)
p = pd.pivot_table()
