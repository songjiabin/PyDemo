import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

"""
供用户通过拖拽指示器 改变变量的值 ，可以水平 也可以 竖直  
"""

# 默认是竖直的     orient=tkinter.HORIZONTAL 变为水平的。
# length 水平是表示宽度  竖直时表示高度
# tickinterval=10 表示刻度为10的倍数

scale = tkinter.Scale(win, from_=0, to=100,
                      orient=tkinter.HORIZONTAL, tickinterval=10, length=200)
scale.pack()


#设置值
scale.set(20)


# 得到当前的值
print(scale.get())


def showNum():
    print(scale.get())
    pass


tkinter.Button(win,text="刻度", command=showNum).pack()

win.mainloop()
