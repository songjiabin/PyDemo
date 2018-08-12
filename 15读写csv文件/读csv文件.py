import csv


# 读csv文件
def readCsv(path):
    infoList = []
    with open(path, "r", encoding='utf-8') as fill:
        # 读所有的文件
        allFileInfo = csv.reader(fill)

        # 拿一行
        for row in allFileInfo:
            infoList.append(row)
            pass
    return infoList


def main():
    path = r"E:\py_project_path\15读写csv文件\淘宝综合数据包.csv"
    info=readCsv(path)
    print(info)
    pass


if __name__ == '__main__':
    main()
