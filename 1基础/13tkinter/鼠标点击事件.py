import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

def fun(event):
    print(event.x,event.y )

# <Button-1> 鼠标左键
# <Button-2> 中间的滚轮
# <Button-3> 鼠标右键

#<Double-Button-1> 鼠标左键双击
# 同理


# <Triple-Button-1> 鼠标左键三连击



button=tkinter.Button(win,text="鼠标点击事件")
button.bind("<Triple-Button-1>",fun)

button.pack()









win.mainloop()