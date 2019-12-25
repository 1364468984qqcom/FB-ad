# -*- coding: utf-8 -*-

import json

str = 'aabbcc'
str1 = json.dumps(str)
print(str1)
print()
print()
print()
dict1 = json.loads(str1)
print(dict1)
print()
print()
print()

dict = {3:5,5:2332,432:344}
for i in dict:
    print(i)