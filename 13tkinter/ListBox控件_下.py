import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
# win.geometry("400x400+200+20")

# 可以使 listBox支持 shift 和 control
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)


for item in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "u", "v", "w", "x", "y", "z"]:
    lb.insert(tkinter.END, item)
    pass

# 添加滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)

lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
sc["command"]=lb.yview



win.mainloop()
