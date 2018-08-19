# 父类是 object
class Person(object):
    # 定义属性  方法
    name = ""
    age = 0
    height = 0
    weight = 0

    # 默认的构造函数
    def __init__(self, name, age, height, weight):
        print("__init___")
        self.name = name;
        self.age = age
        self.height = height;
        self.weight = weight
        pass

    # 定义方法
    # 方法必须第一个参数是 self
    # self 代表类的实例  具体的某个对象
    def eat(self, food):
        print("食物是：", food)

    def run(self):
        print("正在跑的事：",self.name)
        pass

    #当对象释放的时候 自动执行    析构函数
    def __del__(self):
        print("__del__执行了")
        pass

    #当调用__str__的时候 == 当初始化对象 并print(此对象的时候调用)
    def __str__(self):
        return "调用了__str__"
        pass