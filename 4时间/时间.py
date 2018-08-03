import time

# 时间戳 浮点数形式
c = time.time()
print(c)
# tm_year=2018, tm_mon=7, tm_mday=30, tm_hour=12, tm_min=45, tm_sec=0, tm_wday=0, tm_yday=211, tm_isdst=0
# 得到格里尼治时间
print(time.gmtime(c))
# 得到北京时间  时间原组
b = time.localtime(c)
print(time.localtime(c))
# 将本地时间改为时间戳
print(time.mktime(b))
# 将时间元组转出字符串
print(time.asctime(b))
# 将时间戳转成字符串
print(time.ctime(c))
# 将时间元组转换成给定格式的字符串，  参数2为时间元组 如果没有参数2 默认为当前的时间
q=time.strftime("%Y-%m-%d %H:%M:%S", b)
print(q)

#将时间字符串转为时间元组
w=time.strptime(q,"%Y-%m-%d %H:%M:%S")
print(w)

