import threading, time

# 线程调度的
cond = threading.Condition()


def run():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 执行完上面的进行等待....
            cond.wait()
            cond.notify()
        pass
    pass


def run2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 等待通知执行 
            cond.notify()
            cond.wait()
            pass
    pass


if __name__ == '__main__':
    threading.Thread(target=run).start()
    threading.Thread(target=run2).start()
