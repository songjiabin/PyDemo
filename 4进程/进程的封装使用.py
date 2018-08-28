from multiprocessing import Process
import os
import time


# 进程的封装使用

class myProcess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name
        pass

    def run(self):
        print("子进程(%s-%s)启动" % (self.name, os.getpid()))
        time.sleep(0.5)
        print("子进程(%s-%s)结束" % (self.name, os.getpid()))
        pass

    pass
