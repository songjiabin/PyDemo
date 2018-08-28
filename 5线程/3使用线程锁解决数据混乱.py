import threading

num = 100

lock = threading.Lock()


def run(n):
    global num
    for i in range(10000000):
        # 这里进行上锁
        """
        lock.acquire()
        try:
            num = num + n
            num = num - n
        except:
            pass
        finally:
            # 修改完后一定要释放锁
            lock.release()
            pass
        """

        #和上面的功能是一样的。
        with lock:
            num = num + n
            num = num - n






def main():
    t = threading.Thread(target=run, args=(10,))
    t2 = threading.Thread(target=run, args=(8,))
    t.start()
    t.join()
    t2.start()
    t2.join()

    print(num)


pass

if __name__ == '__main__':
    main()
