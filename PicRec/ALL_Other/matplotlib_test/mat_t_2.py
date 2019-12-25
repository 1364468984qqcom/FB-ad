# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(-10, 10, 100)
print(x)
y = x*2 + 55

plt.plot(x, y)
plt.show()
