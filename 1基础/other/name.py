import random

num1, num2 = 6, 7

print(num1, num2)

abc = abs(-10)
print(random.choice([1, 3, 5.6, 54]))

print(random.choice("song"))

if None:
    print("222")
else:
    print(2222)

a = 0
if a and 1:
    print("1")
else:
    print("2")
b = "songjiabin"
print(b[1])

print(b)

print(~12)

num = 10;

print("数据%d" % num)

print("""
who you are 
 Im song
 Ok

""")

bbb = "who you are Im song Ok"

print(bbb.title())

a = [1, 2, 3, 4, 5, 6]
print(len(a))
a.pop(len(a) - 1)
print(a)

print("" != " ")

sut = {1: 1, 2: 2}

print(sut.get(1))


def demo1(num=2, num2=5):
    return (num + num2)


print(demo1())


def demo2(**attr):
    print(attr)


demo2(x=1, y=2)

methon = lambda x, y: x * y

print(methon(43, 34))


# 装饰器




def outter(fun):
    def inner(age):
        if age < 0:
            age = 0
            fun(age)
    return inner;

@outter
def ageMethoh(age):
    print("年龄是：%d" % (age))

ageMethoh(-10)


#通用的装饰





