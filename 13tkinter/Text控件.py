import  tkinter


# 创建窗口
win =tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")


# 显示多行文本    height 代表几行
text=tkinter.Text(win,width=30,height=4)
text.pack()


str="ajmdfkadflajflajfaojflakdjflakjfdlakfklajmdfkadflajflajfaojflakdjflakjfdlakfklajmdfkadflajflajfaojflakdjflakjfdlakfkl;akfa;lfkadfka;dkfa;lfk;a"


text.insert(tkinter.INSERT,str)






win.mainloop()