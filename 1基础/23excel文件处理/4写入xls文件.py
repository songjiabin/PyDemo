# 有序的字典
from collections import OrderedDict
# 写数据  save_data
from pyexcel_xls import save_data


def makeExcelFile(path, data):
    orderedDict = OrderedDict()
    for sheetName, sheetValue in data.items():
        # 从字典里面拿出 key value
        value = {}
        value[sheetName] = sheetValue
        orderedDict.update(value)
        pass
    save_data(path, orderedDict)
    pass


def main():
    # 注意只能保存   .xls 的文件
    path = r"E:\py_project_path\23excel文件处理\res\写入.xls"
    data = {"tab1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "tab2": [["a", "b", "c"], ["e", "f", "g"], ["h", "i", "g"]],
            "tab3": [["a", 1, "c"], ["a", 1, "c"], ["a", 1, "c"]]}
    makeExcelFile(path, data)
    pass


if __name__ == '__main__':
    main()
