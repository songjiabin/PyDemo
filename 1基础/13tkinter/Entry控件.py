import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

"""     
输入控件
"""
# show="*" 输入密码格式
entry = tkinter.Entry(win, show="*")
entry.pack()

# 变量
e = tkinter.Variable();
entry2 = tkinter.Entry(win, textvariable=e)
entry2.pack()
e.set("基本密码就是我");
print(e.get())

tkinter.Button(win, )

# show="*" 输入密码格式

e2 = tkinter.Variable();
entry3 = tkinter.Entry(win, textvariable=e2)
entry3.pack()


def showInfo():
    print(e2.get())


btn = tkinter.Button(win, text="得到上面的数据", width=10, height=2, command=showInfo)
btn.pack()

win.mainloop()
