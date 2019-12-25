# -*- coding: utf-8 -*-
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

"""
font_path='%s/hanyiqihei.ttf' % res_path,改成font_path='hanyiqihei.ttf'
"""
# 打开文本
text = open('D:\\Pro\\CrawlPro\\coding-92\\others\\new 2', encoding='utf-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))
print(text)
print(text[:100])

# 生成对象
# mask = np.array(Image.open("black_mask.png"))
wc = WordCloud(font_path='D:\\Language\\hanzi_show\\simhei.ttf', mode='RGBA', background_color=None).generate(text)
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file('wordcloud4.png')
