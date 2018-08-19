import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

""" 
数值范围控件
"""

# 绑定变量
v = tkinter.StringVar()


def update():
    print(v.get())
    pass


# increment 每次加 或者 减 的数值
# 使用 values=(0,2,4,6,8) 固定显示的数值       最好不用和 from_=-10, to=100 同时使用
sp = tkinter.Spinbox(win, from_=-10, to=100, increment=10,
                     textvariable=v, command=update)
sp.pack()

# 赋值
v.set(20)

# 取值
print(v.get())

sp2 = tkinter.Spinbox(win, increment=10, values=(0, 2, 4, 6, 8))
sp2.pack()

win.mainloop()
