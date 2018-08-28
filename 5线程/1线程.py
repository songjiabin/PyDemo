import threading


# 引入模块
# 1、_thread 低级模块（比较接近底层）
# 2、threading 高级模块（对_thread的封装）

def run():
    print("子线程%s启动" % (threading.current_thread().name))
    pass


def main():
    #  开始进程的时候默认有个线程 （主线程）
    # 主线程可以启动新的字线程
    # 当前线程
    print("主线程%s启动" % (threading.current_thread().name))

    """
    期间可以创建新线程（子线程）
    """
    # name 表示线程的名字
    t = threading.Thread(target=run, name="run1")

    t2 = threading.Thread(target=run)

    t.start()
    t2.start()

    # 等待子线程结束后主线程结束
    t.join()
    t2.join()

    print("主线程%s结束" % (threading.current_thread().name))


if __name__ == '__main__':
    main()
