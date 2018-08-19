import  urllib.request

path=r"E:\py_project_path\2爬虫\res\爬去到的网页直接存入文件.html"
urllib.request.urlretrieve("http://www.jjmima.top",filename=path)


# urlretrieve 在执行的过程中，会产生一些缓存
#清除缓存

urllib.request.urlcleanup()






