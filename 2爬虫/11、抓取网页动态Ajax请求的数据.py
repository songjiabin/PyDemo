import urllib.request
import ssl
import json


# 爬去 ajax的数据
def ajaxCrawler(url):
    heads = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
    }
    req = urllib.request.Request(url, headers=heads)

    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context=context)

    result = response.read().decode("utf-8")
    jsonResult = json.loads(result)

    return jsonResult


def main():
    path = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=time&page_limit=20&page_start=20"
    result = ajaxCrawler(path)
    print(result)
    print(type(result))

    # 进行抓取多个数据

    for i in range(1, 100):
        pathMore = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=time&page_limit=" \
                   "20&page_start=" + str(i * 5)
        resultMore = ajaxCrawler(pathMore)
        print(resultMore)
        pass
    pass


if __name__ == '__main__':
    main()
