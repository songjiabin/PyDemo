import win32api
import win32con
import win32gui


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

    pass


def main():
    path = r"E:\py_project_path\18修改背景图片\res\cafe-3537801__340.jpg"
    setWallPager(path)
    pass


if __name__ == '__main__':
    main()
