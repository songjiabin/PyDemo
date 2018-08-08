from TreeWindows import TreeWindow
import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

path = r"E:\py_project_path"

treeWin = TreeWindow(win, path)

win.mainloop()
