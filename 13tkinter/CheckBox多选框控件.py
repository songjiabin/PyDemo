import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()


def update():
    mesasge = ""
    if hobby1.get() == True:
        mesasge += "复选框1\n"
        pass
    if hobby2.get() == True:
        mesasge += "复选框2\n"
        pass
    if hobby3.get() == True:
        mesasge += "复选框3\n"
        pass
    # 清楚text控件中的数据
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, mesasge)


checkButton1 = tkinter.Checkbutton(win, text="复选框1", variable=hobby1, command=update)
checkButton2 = tkinter.Checkbutton(win, text="复选框2", variable=hobby2, command=update)
checkButton3 = tkinter.Checkbutton(win, text="复选框3", variable=hobby3, command=update)

checkButton1.pack()
checkButton2.pack()
checkButton3.pack()

text = tkinter.Text(win, width=50, height=5)
text.pack()

win.mainloop()
