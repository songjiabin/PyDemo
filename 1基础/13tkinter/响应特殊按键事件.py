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

# <Shift_L> 响应键盘上的 左 Shift
# <Shift_R> 响应键盘上的 右 Shift
# <Return> 响应键盘上回车键
# <BackSpace> 响应键盘上回车键


button.bind("<BackSpace>",fun)






button.pack()












win.mainloop()