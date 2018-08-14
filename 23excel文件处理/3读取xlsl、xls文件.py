# 读取 xls xlsx
# pip install pyexcel     pip install pyexcel-xls


# 有序的字典
from collections import OrderedDict
from pyexcel_xls import get_data


def readXlsFileAndXlsxFile(path):
    # 创建有序的字典
    dic = OrderedDict()
    # 抓取数据 获取的事整体的数据
    xData = get_data(path)

    for sheet in xData:
        dic[sheet] = xData[sheet]
        pass
    return dic


def main():
    # path = r"E:\py_project_path\23excel文件处理\res\b.xlsx"
    path = r"E:\py_project_path\23excel文件处理\res\a.xls"
    result =readXlsFileAndXlsxFile(path)
    print(result)
    pass


if __name__ == '__main__':
    main()
