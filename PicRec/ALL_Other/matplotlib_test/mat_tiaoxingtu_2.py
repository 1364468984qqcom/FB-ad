# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(.5, 1, n)
Y2 = (1 - X / float(n)) * np.random.uniform(.5, 1, n)

plt.figure(figsize=(12, 8))
plt.title('sb')
# 条形图bar
plt.bar(X, +Y1, facecolor='red', edgecolor='black')
plt.bar(X, -Y2, facecolor='green', edgecolor='yellow')

for x, y in zip(X, Y1):
    plt.text(x, y + 0.05, '{}.2f'.format(y), ha='center', va='bottom')

for x, y in zip(X, -Y2):
    plt.text(x, y - .05, '%.2f' % y, ha='center', va='bottom')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
