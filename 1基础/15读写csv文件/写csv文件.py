import csv


# 写csv文件
def writeCsv(path, data):
    with open(path, "w", encoding="utf-8") as fill:
        write = csv.writer(fill)
        # 循环写入 一行一行的写
        for rowData in data:
            write.writerow(rowData)


def main():
    info = [[1, 2, 4], ["这个是", "你", "基本密码"], ["a", "b", "c"]]
    path = r"E:\py_project_path\15读写csv文件\写入文件.csv"
    writeCsv(path, info)


if __name__ == '__main__':
    main()
