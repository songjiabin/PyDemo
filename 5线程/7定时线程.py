import threading, time


def run():
    print("当前线程是%s" % (threading.current_thread().name))
    pass


if __name__ == '__main__':
    # 线程过5秒后才执行呢
    t = threading.Timer(5, run)
    t.start()
    t.join()
