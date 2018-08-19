import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
# win.geometry("400x400+200+20")


scroll = tkinter.Scrollbar()
# 显示多行文本    height 代表几行
text = tkinter.Text(win, width=30, height=4)

text.pack(side=tkinter.LEFT, fill=tkinter.Y)
# sile --> 将滚动条放到窗体的那一侧      fill--> 滚动条是填充X 还是Y方向
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y);

# 进行关联 和滚动条  text.yview 在竖直方向进行关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)




str = "ajmdfkadflajflajfaojflakdjflakjfdlakfklajmdfkadflajflajfaojflakdjflakjfdlakfklajmdfkadflajflajfaojflakdjflakjfdlakfkl;akfa;lfkadfka;dkfa;lfk;a"

text.insert(tkinter.INSERT, str)

win.mainloop()
