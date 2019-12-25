# -*- coding: utf-8 -*-

import multiprocessing as mp
import threading as td
import time


def print_func():
    s_t = time.time()
    list1 = []
    for i in range(1, int(1100000)):
        list1.append(i)
    print(list1)
    e_t = time.time()
    print('运行时间为：', e_t - s_t)


t1 = td.Thread(target=print_func, )
p1 = mp.Process(target=print_func, )
t1.start()
# p1.start()
t1.join()
# p1.join()
p1.run()
print()
print()
print()
print()

def print_func1():
    s_t = time.time()
    list1 = []
    for i in range(1, int(1100000)):
        list1.append(i)
    print(list1)
    e_t = time.time()
    print('运行时间为：', e_t - s_t)


print_func1()
