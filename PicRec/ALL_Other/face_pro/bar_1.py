import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

count = 15

x = np.arange(count)
y1 = (1 - x / float(count)) * np.random.uniform(0.5, 1.0, count)
y2 = (1 - x / float(count)) * np.random.uniform(0.5, 1.0, count)
y3 = (1 - x / float(count)) * np.random.uniform(0.5, 1.0, count)
print(x.ndim)
print(y1.ndim)
print(y2.ndim)
plt.bar(x - 10, abs(y1), facecolor='green', edgecolor='red')
plt.bar(x, y2 - 0.9)
# plt.bar(x, -y3)
plt.show()

"""
创建3个bar，x,y自定义
"""
