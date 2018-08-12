import tkinter
from tkinter import ttk
import os


# Frame
class TreeWindow(tkinter.Frame):

    def __init__(self, master, path, otherWin):

        # 将other放道左边 的Frame中
        self.otherWin = otherWin

        frame = tkinter.Frame(master, width=700, height=500)
        frame.grid(row=0, column=0)
        # frame.pack()
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)

        # 注意  values=(path) 放到这里方便后面得到绝对路径
        root = self.tree.insert("", "end", text=self.getLastPath(path), open=True, values=(path))

        # 开始继续添加新树枝
        self.loadTree(root, path)

        # 给此添加滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # 配置关联
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        # 当点击每个树枝的时候 <<TreeviewSelect>>
        self.tree.bind("<<TreeviewSelect>>", self.itemClick)

    # 每个树枝的点击事件  注意不要忘了 event
    def itemClick(self, event):
        # 1、把名字提取出来
        """

        :event.widget:  触发这个事件的小控件对象
        :return:
        """
        self.v = event.widget.selection()
        # 2、从控件中拿到他展示的text --> fill
        for sv in self.v:
            fill = self.tree.item(sv)["text"]
            # 3、要将此名字放到右边的infoWindow中展示控件中去
            # 给Entry赋值操作
            self.otherWin.ev.set(fill)
            # 接下来要展示具体的文件了 所以需要绝对路径
            apth = self.tree.item(sv)["values"][0]
            print(apth)
            pass
        pass

    def loadTree(self, parentTree, parentPath):
        listDir = os.listdir(parentPath)

        # 遍历所有的文件
        for path in listDir:

            # 如果目录的话进行遍历
            # 拼接路径
            allPath = os.path.join(parentPath, path)

            thisTree = self.tree.insert(parentTree, "end", text=self.getLastPath(allPath),
                                        open=True, values=(allPath))

            if os.path.isdir(allPath):
                self.loadTree(thisTree, allPath)
                pass

    # 切割路径
    def getLastPath(self, path):
        # 其实py中有直接得到后面方法名的方法
        # os.path.splittext(path)
        pathList = os.path.split(path)
        return pathList[-1]
        pass
