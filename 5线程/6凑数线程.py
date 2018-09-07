import threading, time

# 凑够3 才执行呢
#线程数量凑够一定数量才会玩下执行呢

bar = threading.Barrier(2)


def run():
    print("当前的线程：%s开始" % (threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    print("当前线程：%s结束" % (threading.current_thread().name))
    pass


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        pass
