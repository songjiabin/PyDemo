import tkinter

from tkinter import ttk

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("600x400+200+20")

# 表格
tree = ttk.Treeview(win)

# 列
tree["columns"] = ("姓名", "年龄", "身高", "体重")

# 设置每个列  目前列不显示
tree.column("姓名", width=100)
tree.column("年龄", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)

# 真正在表头显示的事  text
tree.heading("姓名", text="姓名-name")
tree.heading("年龄", text="年龄-age")
tree.heading("身高", text="身高-height")
tree.heading("体重", text="体重-weight")

# 添加数据
tree.insert("", 0, text="line1", values=("基本密码", "23", "180", "80"))
tree.insert("", 1, text="line2", values=("卡卡西", "23", "190", "90"))

tree.pack()

win.mainloop()
