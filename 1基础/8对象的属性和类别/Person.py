class Person:
    name = "person"

    def __init__(self, name):
        self.name = name
        pass


def main():
    p=Person("name")
    print(Person.name)

    # 删除对象属性
    del p.name
    # 如果没有对象属性  会去找类属性
    print(p.name)


if __name__ == '__main__':
    main()
