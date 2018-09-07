import threading , time


def func():
    event = threading.Event()

    # 线程所执行的内容
    def run():
        for i in range(4):
            # 线程进行堵塞
            # 等待事件的触发
            event.wait()
            #重置
            event.clear()
            print("打印数据", i)
            pass
        pass

    t = threading.Thread(target=run).start()
    return event


if __name__ == '__main__':
    #为上面的event
    event  = func()
    for i in range(4):
        event.set()
        time.sleep(1)