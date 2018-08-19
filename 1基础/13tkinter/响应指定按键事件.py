import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

#当鼠标释放的时候触发此事件
def fun(event):
    print("响应键盘上的事件")
    pass

button=tkinter.Label(win,text="响应特殊按键事件",bg="red")

#设置焦点
button.focus_set()


#只响应键盘上的 a
button.bind("a",fun)






button.pack()












win.mainloop()