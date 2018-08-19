import urllib.request

#使用爬虫进行网络接口请求

url="http://suggest.taobao.com/sug?code=utf-8&q=%E5%8D%AB%E8%A1%A3&callback=cb"


response = urllib.request.urlopen(url)

data =response.read().decode("utf-8")

print(data)

print(type(data))