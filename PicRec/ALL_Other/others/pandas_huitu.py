import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame, Series

df1 = pd.DataFrame(np.random.randint(1, 40, 20).reshape(4, 5), columns=list('ABCDE'))
print(df1)
# df1.plot()  # 默认折线图
# plt.show()

"""
条形图
"""
# stacked=True堆叠的柱状图
# df1.plot(kind='bar',stacked=True)
# plt.show()
# stacked=False 默认不写
# df1.plot(kind='bar')
# plt.show()
"""
横向条形图
"""
# df1.plot(kind='barh')
# plt.show()
"""
直方图
"""
# df1.plot(kind='hist')
# plt.show()

"""
箱线图
"""
# df1.plot(kind='box')
# plt.show()

"""
密度图
"""

# df1.plot(kind='kde')
# plt.show()

"""
面积图
"""
# df1.plot(kind='area')
# plt.show()

"""
pandas无法做饼图
"""



