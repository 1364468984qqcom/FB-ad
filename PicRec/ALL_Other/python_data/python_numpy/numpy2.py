# -*- coding: utf-8 -*-
import numpy as np

# numpy asarray



a = np.arange(10)
s = slice(2, 9, 3)  # 从索引 2 开始到索引 9 停止，间隔为2
print(a[s])  #[2 5 8]
print()

import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素 #[2 4 5]
print()
print(a[1, ...])  # 第2行元素 #[3 4 5]
print()
print(a[..., 1:])  # 第2列及剩下的所有元素 #[[2 3][4 5][5 6]]