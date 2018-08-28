from multiprocessing import Process
import time
import os

"""
    multiprocessing 跨平台的进程 里面有个 
    process 是进程对象
"""


def run(arges):
    while True:
        print("子进程run()..." + arges + "ip==" + str(os.getpid()))
        time.sleep(0.5)
    pass


def main():
    print("主进程....")

    # 创建子进程
    p = Process(target=run, args=('子进程',))
    p.start()

    while True:
        print("主进程run()...", "id==" + str(os.getpid()))
        time.sleep(0.5)
        pass

    pass


if __name__ == '__main__':
    main()
