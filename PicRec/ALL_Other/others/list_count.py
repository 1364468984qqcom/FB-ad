# list1 = [3, 4, 5, 5, 43, 3, 4]
# a = 0
# for i in list1:
#     b = a^i
#     print(b)
# a, b = 3, 5
# a = a ^ b
# print(a)
# b = a ^ b
# print(b)
#
# a = a ^ b
# print(a)
import time

s = time.time()
list1 = [3, 5555555554, 55, 55, 483, 3, 5555555554]
list2 = list(set(list1))

for i in list2:
    if list1.count(i) == 1:
        print(i)
e = time.time()
print(e - s)
import requests

r = requests.Request('A').P
