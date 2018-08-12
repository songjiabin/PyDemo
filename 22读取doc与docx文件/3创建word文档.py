import os
import win32com
import win32com.client


def makeWordFile(path, name):
    # 调用系统word功能 可以处理 doc 和 docx文件
    mw = win32com.client.Dispatch("Word.Application")
    # 让文件可见
    mw.Visible = True
    # 创建word文档
    doc = mw.Documents.Add()

    # 写内容
    # 从头开始写
    r = mw.Range(0, 0)
    r.InsertAfter("亲爱的" + name + "\n")
    r.InsertAfter("       你还好吗       "+"\n")


    #将文件存储起来
    doc.saveAs(path)

    doc.Close()

    #系统WORD功能关闭
    mw.Quit()

# 创建 名字为 张三 李四 王五  的word文件
def main():
    names = ['张三', '李四', '王五']
    for name in names:
        path = os.path.join(os.getcwd() + "\\res", name)
        makeWordFile(path,name)
        pass
    pass


if __name__ == '__main__':
    main()
