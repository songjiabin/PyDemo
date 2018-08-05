import tkinter


def func():
    print("点击了按钮了......")


# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

# 创建button

button = tkinter.Button(win, text="按钮", width=10, height=2, command=func)

button.pack()

# 当点击按钮的时候这个窗体结束
button2 = tkinter.Button(win, text="结束", command=win.quit)
button2.pack()

win.mainloop()
