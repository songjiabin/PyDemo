import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

# 次模式不能长按鼠标进行拖动
lvb = tkinter.StringVar()
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lvb)

lb.pack()
for item in ["a", "b", "c"]:
    lb.insert(tkinter.END, item)
    pass

# 打印列表中选项
print(lvb.get())

# 将listBox中设置新的值列表
lvb.set((1, 2, 3))


# 绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))
    pass

# 绑定的事 鼠标左键 的双击事件
lb.bind("<Double-Button-1>", myPrint)

win.mainloop()
