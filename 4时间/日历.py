import calendar

"""
 日历模块
"""

#返回指定某年某月的日历
print(calendar.month(2017,8))

#返回指定年的日历
print(calendar.calendar(2018))

#闰年 的判断  闰年返回True 否则返回false
print(calendar.isleap(2018))