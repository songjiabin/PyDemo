# property 其实就是省略了 get set方法 来访问私有属性


class Person:

    def __init__(self, name, age):
        # 将属性进行私有化 添加 __
        self.__name = name
        self.__age = age
        pass

    # 相当于 get方法
    @property
    def age(self):
        return self.__age

    # 相当于 set 方法
    @age.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name;


p = Person("宋佳宾", 24)
p.age = -14
print(p.age)


p.name="我是神经病"

print(p.name)
