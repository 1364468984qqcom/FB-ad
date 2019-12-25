# -*- coding: utf-8 -*-
# 语言列表
language = ['French', 'English', 'German']

# 元组
language_tuple = ('Spanish', 'Portuguese')

# 集合
language_dict = {'Chinese': 44, 'Japanese': 55}
language.extend(language_dict)
print(language)
language.extend(language_tuple)
print(language)
language_set = {44, 55, 66, 777, 2}
language.extend(language_set)
print(language)
