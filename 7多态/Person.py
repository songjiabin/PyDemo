from Anima import Anima
from Cat import Cat
from Mouse import Mouse


class Person(object):

    def __init__(self):
        pass

    def feedAnima(self, Anima):
        Anima.eat()


def main():
    c = Cat("Tom")
    m = Mouse("jerry")
    p = Person()
    p.feedAnima(c)
    p.feedAnima(m)


if __name__ == '__main__':
    main()
