# -*- coding: utf-8 -*-

dict1 = {3: [4, 5, 6], 4: [6, 66, 666], 7: [8, 88], 55: [4, ], 43: [65, 651]}
a = {i: k for k, v in dict1.items() for i in v if len(v) > 2}
# print(a)
b = {v[0]: k for k, v in dict1.items() if len(v) == 2}
c = []
c.append(a)
c.append(b)
print(c)
