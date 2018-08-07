import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

"""
框架控件 
在屏幕上显示一个矩形区域，多作为容器控件 
"""

frm = tkinter.Frame(win);

#创建一个left frame 放到frm中
frm_l = tkinter.Frame(frm)

tkinter.Label(frm_l, text="左上", bg="pink")\
    .pack(side=tkinter.TOP)

tkinter.Label(frm_l, text="左下", bg="blue")\
    .pack(side=tkinter.TOP)

frm_l.pack(side=tkinter.LEFT)


#创建一个 right  frame 放到frm中
frm_r = tkinter.Frame(frm)

tkinter.Label(frm_r, text="右上", bg="yellow")\
    .pack(side=tkinter.TOP)

tkinter.Label(frm_r, text="右下", bg="green")\
    .pack(side=tkinter.TOP)

frm_r.pack(side=tkinter.RIGHT)



frm.pack()

win.mainloop()
