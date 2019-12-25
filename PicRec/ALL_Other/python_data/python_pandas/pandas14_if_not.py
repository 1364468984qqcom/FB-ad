# -*- coding: utf-8 -*-
x = set()

if not x:  # 即x等于None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()时调用，不然不调用
    print(x)
else:
    print(55)

print()
a = {'a': 3, 'b': 35, 'c': 5}
print(a.keys())
for i in a.keys():
    print(i)
from datetime import datetime

day = datetime.now().strftime('%Y-%m-%D')
print(day)
import itertools
print()
for i in itertools.count():
    print(i)
    if i >555:
        break


