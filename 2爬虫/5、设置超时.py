import urllib.request

# 如果网页长时间没有响应，系统判定超时，无法爬去

for i in range(1, 100):
    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.5)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时，爬去失败。继续下一个....")
        pass
    pass
