import threading

# 创建一个全局的ThreadLocal对象
# 每个线程都有独立的存储空间
# 每个线程对ThreadLocal对象都可以读写，但是互不影响


local = threading.local()

num = 0


def run(x, n):
    x = x + n
    x = x - n
    pass


def fun(n):
    # 每个线程都有一个 local.num
    global num
    local.num = num
    for i in range(100000):
        run(local.num, n)
        pass
    pass


if __name__ == '__main__':
    t1 = threading.Thread(target=fun, args=(10,))
    t2 = threading.Thread(target=fun, args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print(num)
