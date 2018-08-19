import tkinter
from tkinter import ttk

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

cv = tkinter.StringVar()

comBox = ttk.Combobox(win, textvariable=cv)
comBox.pack()

# 设置下拉数据
comBox["value"] = ("黑龙江", "北京", "天津")
# 设置默认值
comBox.current(0)


def func(event):
    print(comBox.get())
    # 使用绑定的变量操作它
    print(cv.get())
    pass


# 绑定事件
comBox.bind("<<ComboboxSelected>>", func)

win.mainloop()
