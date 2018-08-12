import sys
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def readPdf(path, toPath):
    # 以二进制打开文件 pdf
    f = open(path, "rb")

    # 创建一个pdf文档分析器
    parser = PDFParser(f)

    # 创建一个pdf文档
    pdfFile = PDFDocument()

    # 连接文档和分析器
    parser.set_document(pdfFile)

    pdfFile.set_parser(parser)


    # 提供初始化密码
    pdfFile.initialize()

    # 检测pdf文档是否提供txt转换
    if not pdfFile.is_extractable:
        # 不提供
        # 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。
        # 一旦执行了raise语句，raise后面的语句将不能执行
        raise PDFTextExtractionNotAllowed

    else:
        # 提供
        manager = PDFResourceManager()
        # 创建一个pdf设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        # 解锁器对象
        interpreter = PDFPageInterpreter(manager, device)

        # 开始循环处理 每次处理一页
        for page in pdfFile.get_pages():
            # 解释这一页
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    # 打开 toPath文件 并 往里面追加 pdf的内容
                    with open(toPath, "a",encoding="utf-8") as f:
                        str = x.get_text()
                        print(str)
                        f.write(str + "\n")


def main():
    path = r"E:\py_project_path\16读取pdf文件\Java 开发接口.pdf"
    toPath = r"E:\py_project_path\16读取pdf文件\Java 开发接口.txt";
    readPdf(path, toPath)


if __name__ == '__main__':
    main()
