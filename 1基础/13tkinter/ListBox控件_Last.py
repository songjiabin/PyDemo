import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")


#多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()

# 向listBox中添加元素

for item in ["good", "nice", "yes", "no"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)



win.mainloop()