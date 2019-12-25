import configparser
import configure
import multiprocessing
import time


# 由mark标记是哪个进程执行的动作
def getkeyWordFunc(queue, lock, mark):
    while not queue.empty():
        # def get(self, block=True, timeout=None):
        keyWord = queue.get()

        # 加锁，是为了防止散乱的打印。 保护一些临界状态
        # 多个进程运行的状态下，如果同一时刻都调用到print，那么显示的打印结果将会混乱
        lock.acquire()
        print(f"keyWord = {keyWord}, markProcess = {mark}")
        lock.release()
        time.sleep(1)


if __name__ == '__main__':
    lock = multiprocessing.Lock()  # 进程锁
    queue = multiprocessing.Queue(150)  # 队列，用于存放所有的初始关键字

    for keyWord, keyWordValue in configure.keySearchWords.items():
        print(f"keyWord = {keyWord}")
        # 如果queue定的太小，剩下的放不进去，程序就会block住，等待队列有空余空间
        # def put(self, obj, block=True, timeout=None):
        queue.put(keyWord)
    print(f"queueBefore = {queue}")

    getKeyProcessLst = []
    # 生成两个进程，并启动
    for i in range(2):
        # 携带的args 必须是python原有的数据类型，不能是自定义的。否则会出现下面的error（见后面）
        process = multiprocessing.Process(target=getkeyWordFunc, args=(queue, lock, i))
        process.start()
        getKeyProcessLst.append(process)

    # 守护线程
    # join 等待线程终止，如果不使用join方法对每个线程做等待终止，那么线程在运行过程中，可能会去执行最后的打印
    # 如果没有join，父进程就不会阻塞，启动子进程之后，父进程就直接执行最后的打印了
    for p in getKeyProcessLst:
        p.join()

    print(f"queueAfter = {queue}")
    queue.close()
    print(f"all queue used.")
