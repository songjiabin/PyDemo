import urllib.request
import random

url = "http://www.baidu.com/"


# 模拟浏览器 1    

"""
# 模拟请求头

heard = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/55.0.2883.87 Safari/537.36"
}

# 设置一个请求体
req = urllib.request.Request(url, headers=heard)

# 发起请求
response = urllib.request.urlopen(req)

# 得到字符串格式的数据
data = response.read().decode("utf-8")

print(data)


"""

# 模拟浏览器 2   不同的User-Agent

urlUserAgentList = [
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "User-Agent: Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
]

# 设置一个请求体
req = urllib.request.Request(url)
randomUrl = random.choice(urlUserAgentList)
# 设置请求头
req.add_header("User-Agent", randomUrl)

response = urllib.request.urlopen(req)

data = response.read().decode("utf-8")

print(data)
