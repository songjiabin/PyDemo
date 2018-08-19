import os, collections


def getAllDirs(path):
    # 创建队列
    queue = collections.deque()
    queue.append(path)

    while len(queue) != 0:
        currentPath = queue.popleft()

        files = os.listdir(currentPath)
        for file in files:
            allPath = os.path.join(currentPath, file)
            if (os.path.isdir(allPath)):
                # 是目录
                print("是目录%s"%(file))
                queue.append(allPath)
                pass
            else:
                # 是文件
                print("是文件%s" % (file))
                pass


getAllDirs(r"E:\py_project_path")
