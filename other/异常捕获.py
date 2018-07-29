
try:
    print(2/0)
except:
    print("异常了")


try:
    print(4/0)
except BaseException as e:
    print("异常")
    pass
finally:
    pass