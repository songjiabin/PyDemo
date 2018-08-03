# 将函数重写写一遍
from 第一个类_1 import Person


# __str__     __repr__

def main():
    p=Person("宋", 20, 177, 80)
    # 调用了 Person 中的  __str__函数
    print(p)



if __name__ == '__main__':
    main()
