import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""
matplotlib 是python
Matplotlib 是一个 Python 的 2D/3D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形 。
通过 Matplotlib，开发者可以仅需要几行代码，便可以生成绘图，直方图，功率谱，条形图，错误图，散点图等


seaborn 是对matplotlib的一种封装（升级）
"""

x = np.linspace(-100, 500, 50)  # 从-1到1 等间距的提取50个数字
# x1 = list('123456789')
print(x)  # 秩为1
y = x ** 2 + 19  # y的取值
print(y)
# plt.figure(num=5,figsize=(100,105))
plt.title('shuzi_zoushitu')  # 标识标题
plt.xlabel('x')  # 给x轴命名
plt.ylabel('y')  # 给y轴命名
# plt.xticks(np.linspace(0, 500, 8))#设置轴的点的数字

# plt.xlim(-120, 500)  # 定义x轴的取值范围
# plt.ylim(0, 25000)  # 定义y轴的取值范围

"""
x:定义x的取值
y:定义y的取值
linestyle：线条风格 '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
linewidth : 线条粗细
color： 颜色
"""

plt.plot(x, y, linestyle=':', linewidth=5, color='red')  # 创建图表的同时将x，y的取值传进去
plt.show()

"""
练习：
    生成曲线             并且将曲线的风格改成 粗细：3，颜色：黄色，风格：solid
"""

"""
10：40上课
"""


