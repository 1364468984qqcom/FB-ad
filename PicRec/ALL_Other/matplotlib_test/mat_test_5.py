# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(3, 5, 20)
y1 = x * 2 + 100
y2 = x ** 2 - 288
y3 = 2 ** x + 1
y4 = 20 * x + 90
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linestyle=':', linewidth=3)

# 给x/y轴添加参数范围
plt.xlim(3, 5)
plt.ylim(-300, 200)

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-200, 0, 100, 200], ['bad', 'normal', 'good', 'really good'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 绑定x轴y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
