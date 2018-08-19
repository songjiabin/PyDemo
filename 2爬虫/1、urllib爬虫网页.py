import urllib.request

# 向指定的url地址发起请求 ，并返回服务器响应的数据（文件的对象）
respose = urllib.request.urlopen("http://www.jjmima.top")

"""
这中读取方式不是很常用

# 得到二进制的数据  读取的事网页中的全部内容    会把读取到的内容赋值给一个字符串变量
data = respose.read()
# 得到 指定编码的数据 data =respose.read().encode("utf-8")

# 将得到的 data存储到文件中
path = r"E:\py_project_path\2爬虫\res\file.html"
with open(path, "wb") as f:
    f.write(data)
"""

"""
#使用这种方式需要循环操作
data =respose.readline()
"""




# 读取文件的全部内容  将读取到的数据给一个列表 变量
data = respose.readlines()
# 需要一行一行的写
path = r"E:\py_project_path\2爬虫\res\基本密码博客.html"
for i in data:
    with open(path, "a") as f:
        f.write(i.decode("utf-8"))

print(data)
print(type(data))
print(len(data))

# 返回当前环境的有关信息
print(respose.info())
# 返回状态码
print(respose.getcode())
# 返回当前正在爬去的url地址
print(respose.geturl())

# 解码
BDurl = r"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%9F%BA%E6%9C%AC%E5%AF%86%E7%A0%81&rsv_pq=ce8b339e0008217c&rsv_t=418bvgyIbahFPS%2F9KJoyaeyIJHdgL55o5LdhC9bHesV4zdD5gye5aJYbmrY&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug1=13&rsv_sug7=101&rsv_sug2=0&inputT=5476&rsv_sug4=6404"
newUrl=urllib.request.unquote(BDurl)
print(newUrl)


#编码
newUrl2=urllib.request.quote(newUrl)
print(newUrl2)