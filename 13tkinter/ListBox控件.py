import tkinter

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

# selectmode : 模式
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()

# 向listBox中添加元素

for item in ["good", "nice", "yes", "no"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)

# 往前面添加
lb.insert(tkinter.ACTIVE, "first")

#添加列表 整个的 不常用
lb.insert(tkinter.END,["very good","添加列表"])


# 删除 列表中的选项  如果不指定参数2的索引，默认删除索引为第一个参数的值

"""
lb.delete(2)
#删除 下标从 1 到  4 的值
lb.delete(1,4)
"""


#选中

lb.select_set(2,4)


#清除选中的
lb.select_clear(3)

# 返回原素的个数
print(lb.size())


#从列表中取值
print(lb.get(0,3))


#得到当前选中的
print(lb.curselection())


#判断 其中的元素是否选中
print(lb.select_includes(2))



win.mainloop()
