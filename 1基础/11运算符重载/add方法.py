
# __add__ 就是运算符重载
class Person(object):

    def __init__(self, num):
        self.__num = num

    def __add__(self, other):
        return self.__num + other.__num


p1 = Person(1)
p2 = Person(2)

print(p1 + p2)
#和上面的事等价的。
print(p1.__add__(p2))





