import threading, time, random, queue


# 生产者
def product(num, q):
    # 生产数据
    while True:
        number = random.randint(0, 10000)
        q.put(number)
        print("存入数据是：%s" % (number))
        time.sleep(3)
    # 完成
    q.task_done()
    pass


# 消费者
def customer(num, q):
    # 从队列中取数据
    while True:
        item = q.get()
        if item is None:
            break
            pass
        pass
        print("取出数据是：%s" % (item))
        time.sleep(3)
    pass
    q.task_done()


if __name__ == '__main__':
    # 消息队列
    q = queue.Queue()

    # 启动生产者
    for i in range(4):
        threading.Thread(target=product, args=(i, q)).start()

    # 启动消费者
    for i in range(4):
        threading.Thread(target=customer, args=(i, q)).start()
        pass
