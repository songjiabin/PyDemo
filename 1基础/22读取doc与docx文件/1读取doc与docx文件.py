import win32com
import win32com.client


def readWordFile(path):
    # 调用系统word功能 可以处理 doc 和 docx文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开word文档
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        #拿出word里面的内容
        line=paragraph.Range.Text
        print(line)
        pass
    #关闭文件
    doc.Close()
    #系统WORD功能关闭
    mw.Quit()

def main():
    path = r"E:\py_project_path\22读取doc与docx文件\res\b.doc"
    readWordFile(path)

if __name__ == '__main__':
    main()
