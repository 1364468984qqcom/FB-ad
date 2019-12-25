import multiprocessing
import datetime


def main():
    pool = multiprocessing.Pool(3)  # 建立进程池，数字为你cpu的核数，括号内可以为空，程序会自动设定为cpu最大核数。
    pool.map(getThesis,)  # 将url传入getThesis函数


def getThesis():
    """this is your code of scrap the url"""


if __name__ == '__main__':
    stime = datetime.datetime.now()
    print(stime)
    main()
    etime = datetime.datetime.now()
    print(etime)
    print(etime - stime)
