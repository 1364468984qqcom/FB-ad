import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# count = 2000
# x = np.random.normal((0, 2, count))
# print(x)
# y = np.random.normal((0, 4, count))
# print(y)
#
# merge1 = np.arctan2(x, y)

# 散点图
# x = [3, 45, 6, 7, 100, 232, 3.32]
# y = [12, -32, 564, 43, 5645, 65, 5.4]
# x = pd.read_excel('/Users/rimi/Desktop/CITY_WEATHER.xlsx')
# y = pd.read_excel('/Users/rimi/Desktop/CITY_WEATHER.xlsx')
# plt.scatter(x, y)
# plt.show()

# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


df1 = pd.read_excel('/Users/rimi/Desktop/CITY_WEATHER.xlsx')
city = df1.groupby(df1['city'])
cd_t = city.get_group('CD')['temperature']
sh_t = city.get_group('SH')['temperature']
sz_t = city.get_group('SZ')['temperature']
bj_t = city.get_group('BJ')['temperature']
# print(bj.ndim) # 秩为1

cd_date = city.get_group('CD')['date']
sz_date = city.get_group('SZ')['date']
bj_date = city.get_group('BJ')['date']
sh_date = city.get_group('SH')['date']
# print(cd_date)


a = plt.scatter(cd_date, cd_t)
b = plt.scatter(sz_date, sz_t)
c = plt.scatter(bj_date, bj_t)
d = plt.scatter(sh_date, sh_t)

plt.xticks(np.linspace(5, 30, 8))
plt.yticks([5, 12, 19, 26, 33, 40], ['cold', 'warm', 'normal', 'hot', 'really hot'])
plt.legend(labels=['cd', 'sh', 'sz', 'bj'], handles=[a, d, b, c])
plt.show()


"""
练习：
    将上图表的边框去掉或者换成其他的颜色   添加标题   给x/y轴重命名   

"""

"""
4：15上课
"""


