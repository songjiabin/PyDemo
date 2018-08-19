from TreeWindows import TreeWindow
from infoWindow import InfoWindow
import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("800x600+200+20")

path = r"E:\py_project_path"

infoWin = InfoWindow(win)

# 将右边Frame放到左边去 方便给右边赋值操作
treeWin = TreeWindow(win, path, infoWin)

win.mainloop()
