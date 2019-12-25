# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# # 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 10, 50)
print(len(x))
print(x)
y = 2 * x + 1

plt.plot(x, y)
plt.plot()
plt.show()
