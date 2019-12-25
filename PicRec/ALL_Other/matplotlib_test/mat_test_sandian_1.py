# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

n = 1024
X = np.random.normal(10, 1, n)
Y = np.random.normal(10, 1, n)
plt.plot(10,10)
T = np.arctan2(X, Y)
plt.scatter(np.arange(50), np.arange(50))

plt.xticks(())
plt.yticks(())
ap = plt.gca()
ap.spines['right'].set_color('none')
ap.spines['top'].set_color('none')
plt.show()
