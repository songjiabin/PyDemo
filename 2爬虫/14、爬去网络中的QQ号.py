import urllib.request
import ssl
import re
import os, collections


# 写字节格式的数据到文件中
def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)
        pass
    pass


def writeFileStr(htmlStr, toPath):
    with open(toPath, "w") as f:
        f.write(str(htmlStr))
        pass
    pass


def getHtmlBytes(url):
    heads = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    }

    req = urllib.request.Request(url, headers=heads)
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context=context)

    return response.read()

    pass


# 爬去指定目录的数据到一个文件中去
def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFileBytes(htmlBytes, r"E:\py_project_path\2爬虫\res\QQ号码\qqFile.html")
    # writeFileStr(htmlBytes, r"E:\py_project_path\2爬虫\res\QQ号码\qqFile.txt")
    htmlStr = str(htmlBytes)
    print(htmlStr)

    # 筛选其中的QQ号
    # ^ 开头的意思 {4,9} 最少5位 最多10位

    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    print(qqsList)
    print(len(qqsList))
    # 去重
    qqsList = list(set(qqsList))
    print(len(qqsList))

    # 将qq数据写到txt文件中
    f = open(toPath, 'a')
    for qqData in qqsList:
        f.write(qqData + "\n")
        pass
    f.close()

    # 匹配网址
    pat = '((http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)'
    re_url = re.compile(pat)
    qqsHttpList = re_url.findall(htmlStr)
    print(qqsHttpList)
    print(len(qqsHttpList))
    # 去重
    qqsList = list(set(qqsHttpList))
    print(len(qqsList))

    return qqsList


def main():
    url = "https://www.douban.com/group/topic/17359302/?start=100 "
    toPath = r"E:\py_project_path\2爬虫\res\QQ号码\QQ.txt"
    # list = qqCrawler(url, toPath)
    # 返回的事里面所有的网址

    deque = collections.deque()
    deque.append(url)

    while len(deque) != 0:
        targetUrl = deque.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            deque.append(tempUrl)
            pass
        pass

    pass


if __name__ == '__main__':
    main()
