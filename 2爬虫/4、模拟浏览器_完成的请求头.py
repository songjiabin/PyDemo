import urllib.request
import random

url = "http://www.baidu.com/"

headers = {'Host': 'example.com',
           'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Accept': 'text/html, */*; q=0.01',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
           'DNT': '1',
           'Referer': 'http://example.com/',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
           }



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
