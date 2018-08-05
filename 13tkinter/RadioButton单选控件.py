import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")


def update():
    #打印其中的value值
    print(r.get())
    pass


# 一组单选框 绑定同一个变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r,command=update)
radio1.pack()

radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r,command=update)
radio2.pack()

win.mainloop()
