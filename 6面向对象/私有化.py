def main():
    p = Person(200)
    p.__money=100
    print(p.getMoney())

    #虽然是私有化  但是 可以用 _类名__属性名 来进行访问
    print(p._Person__money)




#  想要私有化  需在变量前面加上 __   比如 __money
class Person(object):
    money = 0

    def __init__(self, money):
        self.__money = money;

    def getMoney(self):
        return self.__money

    def setMoney(self, money):
        self__money = money


if __name__ == '__main__':
    main();
