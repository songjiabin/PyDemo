# 扒取一号店女装
import urllib.request
import ssl
import re
import os


def imageCrawler(url, toPath):
    heads = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
    }

    req = urllib.request.Request(url, headers=heads)

    response = urllib.request.urlopen(req)

    htmlStr = response.read().decode("utf-8")

    """
    # 将html数据写入文件

    with open(r"E:\py_project_path\2爬虫\res\一号店.html", "wb") as f:
        f.write(htmlStr)

    print(htmlStr)

    """

    # 提出正则
    pat = r'<div style="position: relative">\n<img src="//(.*?)/>'

    re_d = re.compile(pat, re.S)
    list = re_d.findall(htmlStr);
    print(list)
    print(len(list))

    num = 1
    for imageUrl in list:
        # 拿出 里面的图片并存储到文件中
        path = os.path.join(toPath, str(num) + ".jpg")
        num += 1
        # 将图片下载到本地
        urllib.request.urlretrieve("http://" + imageUrl, filename=path)
        pass


def main():
    url = r"http://search.yhd.com/c9712-0-0"
    toPath = r"E:\py_project_path\2爬虫\res\女装"
    imageCrawler(url, toPath)


if __name__ == '__main__':
    main()
