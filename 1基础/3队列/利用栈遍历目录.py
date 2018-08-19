import os


def getAllDirs(path):
    fileList = []
    fileList.append(path)
    # 当栈中有数据的话进行操作
    while len(fileList) > 0:
        currentFile = fileList.pop()
        files = os.listdir(currentFile)
        for file in files:
            if (os.path.isdir(os.path.join(currentFile, file))):
                #判断是不是目录 是的话 将目录入栈
                print("是目录%s"%(file))
                fileList.append(os.path.join(currentFile, file))
                pass
            else:
                # 是文件的话 进行打印  并出栈
                print("是文件%s"%(file))
                pass


getAllDirs(r"E:\py_project_path")
