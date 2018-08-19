import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

# 创建label
# bg = 背景颜色
# fg = 字体颜色    font=("字体",字体的大小)  width 宽度  height 高度    wraplength 大于100换行
# justify 靠哪里对齐  anchor (n:北  e:东   s:南   w:西  center:中心)
label = tkinter.Label(win, text="label",
                      bg="red",
                      fg="green",
                      font=("黑体", 20),
                      width=100,
                      height=4,
                      wraplength=100,
                      justify="right",
                      anchor="center"
                      )
# 显示出来
label.pack()

win.mainloop()
