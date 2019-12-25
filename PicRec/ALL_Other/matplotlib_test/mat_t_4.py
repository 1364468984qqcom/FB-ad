from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(3, 44, 50)
y1 = x * 2 + 100
y2 = x ** 2 - 14
y3 = y1 * 100 - 1000
y4 = x * 5 - 1000
y5 = x + x + 100
plt.xlabel('I AM X')
plt.ylabel('I AM Y')
plt.plot(x, y1)
plt.plot(x, y2, color='red', linestyle=':', linewidth=2)
plt.plot(x, y3, color='green', linestyle='--', linewidth=4)
plt.plot(x, y4, color='black', linewidth=6, linestyle=':')
plt.plot(x, y5, color='yellow', linestyle=':', linewidth=1)
plt.show()
