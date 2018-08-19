import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

#当鼠标释放的时候触发此事件
def fun(event):
    print(event.x,event.y)
    pass

button=tkinter.Button(win,text="鼠标释放事件")
button.bind("<ButtonRelease-1>",fun)

button.pack()

win.mainloop()