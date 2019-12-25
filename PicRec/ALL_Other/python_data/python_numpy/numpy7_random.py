# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(12345)
nsteps = 1000
drwas = np.random.randint(0, 2, size=nsteps)
steps = np.where(drwas > 0, 1, -1)
print(steps)
print()
print()
print()
walk = steps.cumsum()
print(walk)
print()
print()
print()

walk.min()
print(walk.min())
print()
print()
print()
walk.max()
print(walk.max())
print()
print()
print()
t = (np.abs(walk) >= 10).argmax()
print(t)