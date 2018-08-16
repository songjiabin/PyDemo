from functools import reduce


# reduce(fn,lsd)
# 参数1 为函数
# 参数2 为列表
# 功能： 一个函数作用在序列上。这个函数必须接受两个参数。
# reduce把结果继续和序列的下一个元素累计运算

# 如 reduce(fun,[a,b])


def main():
    list = [1, 2, 3, 4, 5]
    result =reduce(addFun,list)
    print(result)


def addFun(num1, num2):
    return num1 + num2
    pass


if __name__ == '__main__':
    main()
