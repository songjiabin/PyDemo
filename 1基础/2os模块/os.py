import os

"""
 os 包含了普遍操作系统的模块
"""


# 操作系统的名字  nt-> window
print(os.name)
# 打印操作系统的详细详细  window 不支持
# print(os.uname)
# 获取操作系统的所有环境变量
print(os.environ)
# 获取操作系统的所有环境变量的中具体的某个  指定得到具体的环境变量
print(os.environ.get("ANDROID_HOME"))
# 获得当前的目录
print(os.curdir)
# 获取当前工作目录  即 当前python脚本所在的目录
print(os.getcwd())
# 获得指定目录下面的目录的所有的文件（包含文件）
print(os.listdir(r"E:\py_project_path"))
# 在当前目录下创建新的文件
os.makedirs("os创建的目录")
# 删除指定目录
os.rmdir("os创建的目录")
# 改名字给目录
# os.rename("os创建的目录","os创建的目录2")
# 删除普通文件
# os.remove(r"E:\py_project_path\2os模块\1.txt")
#调用系统notepad
# os.system("notepad")
#查看当前的绝对路径
print(os.path.abspath("."))
#判断是否是目录
print(os.path.isdir(r"E:\py_project_path\2os模块"))
#判断文件是否存在
print(os.path.isfile(r"E:\py_project_path\2os模块\1.txt"))
# 判断目录是否存在
print(os.path.exists(r"E:\py_project_path\2os模块"))
# 获得文件的大小 （字节）
print(os.path.getsize(r"E:\py_project_path\2os模块\1.txt"))
# 获得文件目录
print(os.path.dirname(r"E:\py_project_path\2os模块\1.txt"))
# 获得文件名字
print(os.path.basename(r"E:\py_project_path\2os模块\1.txt"))