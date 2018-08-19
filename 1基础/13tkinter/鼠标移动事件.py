import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

def fun(event):
    print(event.x,event.y )



#当鼠标在控件上长按左键时移动使用
button=tkinter.Button(win,text="鼠标移动事件")
button.bind("<B1-Motion>",fun)

button.pack()









win.mainloop()