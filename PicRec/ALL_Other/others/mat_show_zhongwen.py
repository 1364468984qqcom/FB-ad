import matplotlib.pyplot as plt
from matplotlib import font_manager

font = font_manager.FontProperties(fname='C:\Windows\Fonts\SIMHEI.TTF')

x = [3, 45, 6]
y = [5, 6, -33]
plt.plot(x, y, ':', 'r')
plt.title('曲线', fontproperties=font)
plt.xlabel('x轴', fontproperties=font)
plt.ylabel('y轴', fontproperties=font)
plt.show()
print()

# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import pylab as mpl  # import matplotlib as mpl

# 设置汉字格式
# sans-serif就是无衬线字体，是一种通用字体族。
# 常见的无衬线字体有 Trebuchet MS, Tahoma, Verdana, Arial, Helvetica,SimHei 中文的幼圆、隶书等等
# mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# 画出散点图，散点颜色为红色，大小为20,透明度为0.7
plt.scatter([1, 2, 3, 4, 5, 6], [2, 3, 4, 6, 9, 12], color='r', s=20, alpha=.7)
# 设置轴的区间
plt.axis([0, 8, 0, 20])
# 设置中文标签
plt.title(u"散点图测试")
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
# 显示图片
# plt.show()
