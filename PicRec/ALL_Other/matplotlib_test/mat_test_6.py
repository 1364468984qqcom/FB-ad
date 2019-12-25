# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd

import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = 2 ** x + 1
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='green', linestyle=':', linewidth=2)
plt.xlim((-1, 2))
plt.ylim((1, 3))

# 设置点的位置
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1, 0, 1.2, 3], ['really bad', 'bad', 'normal', 'good', 'really good'])
ax = plt.gca()
# 将右边和上边的边框（脊）的颜色去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 绑定x轴，y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 定义x轴y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
