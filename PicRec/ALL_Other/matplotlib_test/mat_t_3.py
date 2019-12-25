# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

x = np.linspace(0, 23, 50)
y1 = 2 * x * 2 + 10
y2 = x ** 2 + 2

# 使用figure()函数重新申请一个figure对象
plt.figure()
plt.plot(x, y1)
plt.figure(num=3, figsize=(8, 5))

# 当我们需要在画板中绘制两条线的时候，可以使用下面的方法：
plt.plot(x, y2)
plt.plot(x, y1, color='blue', linewidth=5.0, linestyle='dotted')
plt.show()
