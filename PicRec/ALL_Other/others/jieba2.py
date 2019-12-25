import jieba.posseg as jg

word = '我去过上海浦东新区东方明珠'

res1 = jg.cut(word)
for i in res1:
    print(i.word, '------------', i.flag)
