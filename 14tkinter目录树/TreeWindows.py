import tkinter
from tkinter import ttk
import os


# Frame
class TreeWindow(tkinter.Frame):

    def __init__(self, master, path):
        frame = tkinter.Frame(master)
        frame.pack()
        self.tree = ttk.Treeview(frame)
        self.tree.pack()

        root = self.tree.insert("", "end", text=self.getLastPath(path), open=True)

        # 开始继续添加新树枝
        self.loadTree(root, path)

    def loadTree(self, parentTree, parentPath):
        listDir = os.listdir(parentPath)

        # 遍历所有的文件
        for path in listDir:
            thisTree = self.tree.insert(parentTree, "end", text=self.getLastPath(path), open=True)

            # 如果目录的话进行遍历
            # 拼接路径
            allPath = os.path.join(parentPath, path)
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
