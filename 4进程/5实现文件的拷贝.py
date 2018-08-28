import os
from multiprocessing import Pool
import time


# 实现文件的拷贝
def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    pass


def thread():
    start = time.time()

    rPath = r"E:\py_project_path\4进程\res\file"
    toPath = r"E:\py_project_path\4进程\res\tofile"

    pool = Pool(2)

    # 读取目录下的所有文件
    listDir = os.listdir(rPath)
    for fileName in listDir:
        absPath = os.path.join(rPath, fileName)
        absToPath = os.path.join(toPath, fileName)
        pool.apply_async(copyFile, (absPath, absToPath))

        pass

    pool.close()
    pool.join()

    end = time.time()
    print("总耗时%0.2f" % (end - start))
    pass


def main():
    start = time.time()

    rPath = r"E:\py_project_path\4进程\res\file"
    toPath = r"E:\py_project_path\4进程\res\tofile"

    # 读取目录下的所有文件
    listDir = os.listdir(rPath)
    for fileName in listDir:
        absPath = os.path.join(rPath, fileName)
        absToPath = os.path.join(toPath, fileName)
        copyFile(absPath, absToPath)
        pass

    end = time.time()

    print("总耗时%0.2f" % (end - start))
    pass


if __name__ == '__main__':
    # 在主线程中
    main()

    # 在线程中
    # thread()
pass
