from multiprocessing import Pool
import os
import time


def run(name):
    print("启动子进程%d,id是%s"%(name, str(os.getpid())))
    time.sleep(0.5)
    print("结束子进程%d,id是%s"%(name, str(os.getpid())))
    pass


def main():
    print("启动主进程")

    # 创建多个进程
    # 进程池
    # 表示可以同时执行的进程数量 默认为CPU的核数
    pool = Pool(2)

    for i in range(5):
        # 创建进程，放入进程池统一管理
        pool.apply_async(run, args=(i,))


    # 注意在进行join之前必须先close
    # 一旦colse就不能添加新的进程了

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
