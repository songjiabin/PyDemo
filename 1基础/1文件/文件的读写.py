#  文件的读
path = r"E:\py_project_path\demo.txt"

# f=open(path,"r")
#
# content =f.read()
# print(content)
#
#
# f.close()


# 简单的方式
# r表示是文本文件，rb是二进制文件
with open(path, "r")  as  f1:
    print(f1.read())

# 文件的写
# writePath=r"E:\py_project_path\write.txt"
# f2 =open(writePath,"w",encoding="utf-8")
# f2.write("这个是我写的内容哦")
# f2.flush()


writePath = r"E:\py_project_path\write.txt"

with  open(writePath, "w", encoding="utf-8") as f3:
    f3.write("三生三世")
