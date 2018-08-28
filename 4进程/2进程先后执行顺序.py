from multiprocessing import Process
import time
import os

"""
    multiprocessing 跨平台的进程 里面有个 
    process 是进程对象
"""


def run(arges):
    print("子进程run()..." + arges + "ip==" + str(os.getpid()))
    print("子进程结束")


def main():
    print("主进程....")

    # 创建子进程
    p = Process(target=run, args=('子进程',))



    p.start()



    #如果我想让主进程等待子进程。当子进程结束后再执行主进程 join()方法就是这个
    p.join()
    print("主进程结束...")



    pass


if __name__ == '__main__':
    main()
