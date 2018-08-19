# pip install pygame


import time
import pygame


def main():
    path = r"E:\py_project_path\17播放音乐\res\Dreamhouse - Sha-La-La.mp3"
    # 初始化
    pygame.mixer.init()
    # 加载音乐
    track = pygame.mixer.music.load(path)
    # 播放
    pygame.mixer.music.play()
    #需要他进程执行下
    time.sleep(5)
    #播放5秒后暂停
    pygame.mixer.music.pause()

    pygame.mixer.music.stop()


    pass

if __name__ == '__main__':
    main()
