import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

menubar = tkinter.Menu(win)
win.config(menu=menubar)


def update():
    print("###")
    pass


# 创建一个菜单
menu1 = tkinter.Menu(menubar, tearoff=False)

for item in ["A", "B", "C", "退出"]:
    if item == "退出":
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
        pass
    else:
        menu1.add_command(label=item, command=update)
        pass
    pass

menubar.add_cascade(label="字母", menu=menu1)

# 创建另外一个菜单
menu2 = tkinter.Menu(menubar, tearoff=False)

for item in ["red", "blue", "green", "yellow"]:
    if item == "退出":
        menu2.add_command(label=item, command=win.quit)
        pass
    else:
        menu2.add_command(label=item, command=update)
        pass
    pass

menubar.add_cascade(label="颜色", menu=menu2)

win.mainloop()
