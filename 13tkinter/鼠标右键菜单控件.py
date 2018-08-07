import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

# 创建一个菜单

menubar = tkinter.Menu(win)

menu1 = tkinter.Menu(menubar, tearoff=False)

for item in ["A", "B", "C", "退出"]:
    if item == "退出":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
        pass
    else:
        menu1.add_command(label=item)
        pass
    pass

menubar.add_cascade(label="字母", menu=menu1)


def showMenu(event):
    menubar.post(event.x_root, event.y_root)
    pass


win.bind("<Button-3>", showMenu)

win.mainloop()
