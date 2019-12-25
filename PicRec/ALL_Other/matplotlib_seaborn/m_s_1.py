import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style(style='whitegrid')
sns.set_context(context='poster', font_scale=1.8)  # 整体和放大
sns.set_palette(palette='summer')  # 颜色
df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('ABCD'))
print(df1)
plt.title('Bar')
plt.xlabel('A')
plt.ylabel('B')
plt.axis([0, 4, 0, 10])
plt.xticks(np.arange(len(df1['A'].value_counts())) + .5, df1['B'].value_counts().index)
plt.bar(np.arange(len(df1['A'].value_counts())) + .5, df1['B'].value_counts(), width=.3)

plt.show()
