import threading, time

# 控制并发的数量是2
sem = threading.Semaphore(2)


def run():
    with sem:
        print("当前线程%s" % (threading.current_thread().name))
        time.sleep(3)
    pass


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        pass
