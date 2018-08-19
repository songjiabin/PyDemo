import time
import pygame

import win32api
import win32con
import win32gui

import threading


# 循环播放音乐
def go():
    print("go")
    pygame.mixer.init()
    # 循环播放音乐
    while True:
        for i in range(3):
            fillPath = r"E:\py_project_path\19整蛊小程序\res" \
                       + "\\" + str(i + 1) + ".mp3"
            # 加载音乐
            track = pygame.mixer.music.load(fillPath)
            # 播放
            pygame.mixer.music.play()
            time.sleep(3)
            pygame.mixer.music.stop()
            pass
    pass

#修改背景
def backPager():
    print("backPager")
    while True:
        for i in range(3):
            fillPath = r"E:\py_project_path\19整蛊小程序\res" \
                       + "\\" + str(i + 1) + ".jpg"
            setWallPager(fillPath)
    pass


# 设置背景
def setWallPager(path):
    # 打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop"
                                    , 0, win32con.KEY_SET_VALUE)
    # 设置 是否拉伸...等
    # 2 拉伸  0 居中  6 自适应  10填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2");

    # 设置图片
    # win32api.RegSetValueEx(reg_key, "WallPaper")

    # 背景图片   SPIF_SENDWININICHANGE->立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
    time.sleep(3)
    pass


def main():
    th = threading.Thread(target=go, name="LoopThread")
    th.start()

    th2 = threading.Thread(target=backPager, name="OhterThread")
    th2.start()

    pass


if __name__ == '__main__':
    main()
