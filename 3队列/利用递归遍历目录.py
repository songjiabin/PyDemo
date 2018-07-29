import os


def getAllDirs(path, pc=" "):
    pc += " "
    # 得到当前目录下的所有文件
    filesList = os.listdir(path)
    for file in filesList:
        # 遍历得到所有的目录
        if (os.path.isdir(os.path.join(path, file))):
            print(pc + "是目录", file)
            getAllDirs(os.path.join(path, file), pc )
        else:
            print(pc + "是文件", file)


getAllDirs(r"E:\py_project_path")
