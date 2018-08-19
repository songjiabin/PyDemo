import win32com
import win32com.client


def readWordFile(path,toPath):
    # 调用系统word功能 可以处理 doc 和 docx文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开word文档
    doc = mw.Documents.Open(path)

    doc.SaveAs(toPath,2)#2 表示为txt文件

    #关闭文件
    doc.Close()
    #系统WORD功能关闭
    mw.Quit()

def main():
    path = r"E:\py_project_path\22读取doc与docx文件\res\b.doc"
    toPath=r"E:\py_project_path\22读取doc与docx文件\res\other.txt"
    readWordFile(path,toPath)

if __name__ == '__main__':
    main()
