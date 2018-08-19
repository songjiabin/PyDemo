# 通用的装饰


def outer(fun):
    def inner(*attr, **attrs):
        print("装饰器在这里呢....")
        fun(*attr, **attrs)
        pass

    return inner;


@outer
def say(name, age):
    print("我的名字是：%s,年龄是：%s" % ("宋佳宾", 18))


@outer
def say2(**attrs):
    print(attrs)


say("宋佳宾", 18)
say2(a=1, b=2)
