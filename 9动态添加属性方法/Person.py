from types import MethodType


class Person(object):
    # 限制属性 不能乱写了就  属性名字 只能是这些
    __slots__ = ("name", "b", "newMethoh")


p = Person()

# 动态添加 属性
p.name = "person"

print(p.name)


def say(self):
    print("动态添加的方法名字是：", self.name)
    pass


# 动态添加方法  不建议这么搞
p.b = say
p.b(p)

# 将方法赋值给新的 newMethoh  建议使用这个
p.newMethoh = MethodType(say, p)
p.newMethoh()
