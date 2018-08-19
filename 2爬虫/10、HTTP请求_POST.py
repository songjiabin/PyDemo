import urllib.request
import urllib.parse

# 使用爬虫进行网络接口请求

url = "http://v.juhe.cn/xianxing/citys"

# 将需要发送的数据整合成一个字典
data = {
    "key": "7b79ea34ed40b45962a3cbe39a46d720"
}

# 将发送的数据打包
postData = urllib.parse.urlencode(data).encode("utf-8")

# 请求体
req = urllib.request.Request(url, postData)

# 请求

req.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)")

repose = urllib.request.urlopen(req)

dataString =repose.read().decode("utf-8")

print(dataString)