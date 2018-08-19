"""
原型：filter(fun,lsd)
参数 1  函数
参数 2  为序列
"""

# 功能 用于过滤序列
# 就是讲序列中的每个元素放到方法中进行条件过滤

list1 = [1, 2, 3, 4, 5, 6]


def fun(num):
    if num % 2 == 0:
        # 返回True  f复合条件
        return True
    else:
        # 不符合
        return False;

    pass


def main():
    #找出复合偶数的值
    resultList = filter(fun, list1)
    print(list(resultList))

    pass


if __name__ == '__main__':
    main()
