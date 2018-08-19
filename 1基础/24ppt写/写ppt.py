import win32com
import win32com.client


def makePPT(path):
    ppt = win32com.client.Dispatch("Word.Application")
    ppt.Visible = True

    # 添加一个文件
    pptFile = ppt.Presentations.Add()

    # 创建页  参数1 是第一页开始  参数2 为类型 
    page1 = pptFile.Slides.Add(1, 1)

    # page1.Shapes[0] 获取 框
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "基本密码"

    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "content"

    # 保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()


    pass


def main():
    path = r"E:\py_project_path\24ppt写\res\a.ppt"
    makePPT(path)
    pass


if __name__ == '__main__':
    main()
