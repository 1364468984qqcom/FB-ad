from multiprocessing import Pool
import time


def func1(a):
    now_time = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
    print(now_time)
    print(a)


if __name__ == '__main__':
    for i in range(600):
        func1(i)
    # print('开始......')
    # pool = Pool(6)
    # for i in range(6000):
    #     pool.apply_async(func1, args=(i,))
    # pool.close()
    # pool.join()
