import urllib.request
import ssl
import re


# 爬去 糗事百科的数据 ajax的数据
def ajaxCrawler(url):
    heads = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
    }

    req = urllib.request.Request(url, headers=heads)

    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context=context)

    html = response.read().decode("utf-8")

    print(html)

    # 写入html
    """   
    path = r"E:\py_project_path\2爬虫\res\糗事百科.html"
    with open(path, "w") as f:
        f.write(html)
    """

    # 找到里面特定的内容  比如段子  需要用正则表达式

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'

    # 编译
    re_joke = re.compile(pat, re.S)

    divList = re_joke.findall(html)
    print(divList)
    print(len(divList))

    print("------------------------------------------------------")
    dict = {}
    # 得到作者 和 内容以后     进一步提出来里面内容
    for div in divList:
        # 因为作者的名字是<h2/>包含的 所以对h2进行查找
        re_u = re.compile(r'<h2>(.*?)</h2>', re.S)
        userName = re_u.findall(div)
        name = userName[0]

        # 段子  r'<div class="content">\n<span>(.*?)</span>' 匹配中间的数据
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        userContent = re_d.findall(div)

        content = userContent[0]

        dict[name] = content

        pass

    print(dict)
    return dict


def main():
    allList=[]
    for i in range(1, 10):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        dict = ajaxCrawler(url)
        allList.append(dict)
        pass
    print(allList)
    print(len(allList))
    pass


if __name__ == '__main__':
    main()
