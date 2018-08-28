from multiprocessing import Process, Queue
import os


# 进程间的通信


def read(q):
    print("进程读启动%s" % (os.getpid()))

    while True:
        value = q.get(True)
        print(value)
        pass

    print("进程读结束%s" % (os.getpid()))
    pass


pass


def write(q):
    print("进程写启动%s" % (os.getpid()))

    for char in ['a', 'b', 'c']:
        # 像队列里面写数据
        q.put(char)
        pass

    print("进程写结束%s" % (os.getpid()))
    pass


def main():
    # 父进程创建队列并传递给子进程
    q = Queue()
    # 读的进程
    pr = Process(target=read, args=(q,))
    # 写的进程
    pw = Process(target=write, args=(q,))

    pr.start()
    pw.start()

    pw.join()
    # 当pw进程结束后才 结束 pr进程
    pr.terminate()

    print("主进程结束")

    pass


if __name__ == '__main__':
    main()
