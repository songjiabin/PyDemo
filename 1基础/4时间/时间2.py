import time

#开始计时
time.clock()
for i in range(100000):
    pass
#结束计时 共用了多久
print(time.clock())


