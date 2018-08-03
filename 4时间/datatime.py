# 比 time 更加牛逼  可以说是time的封装版本

import datetime

"""
模块中的类 
datetime        同时用时间和日期 （***）  
timedelta       主要用于计算时间的跨度
tzinfo          时区相关
time            只关注时间
data            只关注日期
"""

# 获取当前时间
d1 = datetime.datetime.now()
print(d1)

# 获取指定时间
d2 = datetime.datetime(1992, 1, 17, 11, 23, 34, 234234);
print(d2)

# 将时间转为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# 将字符串转为 datetime对象
# 注意：转换的格式要与字符串一致
d4=datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)



