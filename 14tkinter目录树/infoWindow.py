import tkinter
from tkinter import ttk
import os


# 点击左边的目录树展示到右边  右边的Frame
class InfoWindow(ttk.Frame):

    def __init__(self, master):
        frame = tkinter.Frame(master)
        #放大右边
        frame.grid(row=0, column=1)

        #创建输入控件
        #给entry绑定变量
        self.ev = tkinter.Variable();
        self.entry=tkinter.Entry(frame,textvariable=self.ev)
        self.entry.pack()

        #文本控件
        self.text=tkinter.Text(frame)
        self.text.pack()






        pass
