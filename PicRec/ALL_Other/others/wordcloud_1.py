import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


"""
词云图
"""
test = open('D:\\Pro\\CrawlPro\\coding-92\\others\\new 1', encoding='utf-8').read()
wc = WordCloud().generate(text=test)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
wc.to_file('word_cloud.png')
