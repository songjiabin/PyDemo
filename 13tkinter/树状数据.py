import tkinter
from tkinter import ttk

# 创建窗口
win = tkinter.Tk();
# 创建标题
win.title("基本密码")
# 设置大小的
win.geometry("400x400+200+20")

tree = ttk.Treeview(win)

# 添加一级树枝
tree1 = tree.insert("", 0, "中国", text="中国CHI", values=("F1"))

tree2 = tree.insert("", 1, "美国", text="美国USA", values=("F2"))

tree3 = tree.insert("", 2, "英国", text="英国UK", values=("F3"))

# 添加二级树枝

tree1_1=tree.insert(tree1, 0, "黑龙江", text="中国黑龙江", values=("F1_1"))

tree.insert(tree1, 1, "吉林", text="中国吉林", values=("F1_2"))

tree.insert(tree1, 2, "山东", text="中国山东", values=("F1_3"))





#二级树枝
tree.insert(tree2, 0, "费城", text="美国费城", values=("F2_1"))

tree.insert(tree2, 1, "加州", text="美国加州", values=("F2_2"))

tree.insert(tree2, 2, "休斯顿", text="美国休斯顿", values=("F2_3"))



tree.insert(tree1_1, 0, "A省", text="中国黑龙江A省", values=("F1_1_1"))
tree.insert(tree1_1, 1, "B省", text="中国黑龙江B省", values=("F1_1_2"))
tree.insert(tree1_1, 2, "C省", text="中国黑龙江C省", values=("F1_1_3"))







tree.pack()

win.mainloop()
