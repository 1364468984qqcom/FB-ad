# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()  # 新建一个图形
ax = Axes3D(fig)

# plt.savefig('fig.png', bbox_inches='tight')
# 生成x/y轴
X = np.arange(-4, 4, .25)
Y = np.arange(-4, 4, .25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# 行的跨度  和列的跨度 以及颜色映射样式
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

# offset 表示zdir的轴距离
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0, 0)
plt.savefig('3D_1.jpg')
plt.show()
