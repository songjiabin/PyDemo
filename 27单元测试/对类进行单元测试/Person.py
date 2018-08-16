class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 得到类中变量的值
    def getAge(self):
        return self.age
