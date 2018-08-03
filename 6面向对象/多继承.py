from 多继承_father import Father
from 多继承_mother import Mother


class my(Father, Mother):

    def __init__(self, name, age, money, faceValue):
        # 调用父类的 构造方法
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)
        pass

    #重写父类的方法
    def play(self):
        print("I im playing")
        pass

def main():
    m= my("宋佳宾",25,10000,100)
    m.cook()
    m.work()
    m.play()

if __name__ == '__main__':
    main()