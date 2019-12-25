import gensim
import html5lib
import pandas as pd


df1 = pd.read_html('https://slamdunk.sports.sina.com.cn/player/rank#season_type=reg&item_type=average&item=points')
print(type(df1))
print(df1[0])
