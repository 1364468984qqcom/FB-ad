# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

array1 = np.array([2.645, 3.231, 4.2, 5.2, 6.05, 3.27, 8.9, 1.2008, 41.2, 52.2, 26.235, 42.03]).reshape(3, 4)
# 主要使用imshow来显示图片，这里暂时不适用图片来显示，采用色块的方式演示。
plt.imshow(array1, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.9)  # 这是颜色深度的标注，shrink表示压缩比例
plt.xticks(())
plt.yticks(())
plt.show()
