import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

#当鼠标释放的时候触发此事件
def fun(event):
    print("event.char",event.char)
    print("event.keycode", event.keycode)
    pass

button=tkinter.Label(win,text="响应所有事件",bg="red")

#设置焦点
button.focus_set()

#<Key> 响应所有键盘上的值
button.bind("<Key>",fun)

button.pack()

win.mainloop()