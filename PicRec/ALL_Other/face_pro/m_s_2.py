import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

x = np.linspace(-1, 5, 50)  # 从0到5等间距的提取50个数字
# x1 = list(1234567890134)
# print(x)  # 秩为1

y1 = x ** 4 - 100
y2 = 10 * x + 100
plt.xlabel('month')  # 定义x轴的重命名

plt.ylabel('salary')  # 给y轴重命名
plt.title('jiao_hui:')  # 图表标题
b, = plt.plot(x, y1, color='yellow', linestyle='--', linewidth=2.5)
a, = plt.plot(x, y2, color='red', linestyle=':', linewidth=4)

plt.xticks(np.linspace(-5, 5, 10))  # 定义x轴的取值范围
plt.yticks([-300, -100, 0, 100, 300, 500], ['None', 'really bad', 'bad', 'normal', 'good', 'really good'])
ax = plt.gca()  # 作用：去掉边框/命名等修饰操作
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
"""
left,bottom
"""
# plt.show()
#  绑定x轴y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 定义x轴y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

"""
练习：
    创建一个图表，同时显示2条曲线，不去将bottom和top边框去掉/改颜色
"""
plt.legend(labels=['y1', 'y2'], handles=[b, a], loc='best')
plt.show()

"""
创建图表，显示2条曲线的名称
"""
