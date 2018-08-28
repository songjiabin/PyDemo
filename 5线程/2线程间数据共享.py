import threading

num = 0


def run(n):
    global num
    for i in range(10000000):
        num = num + n
        num = num - n
        pass
    pass


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
