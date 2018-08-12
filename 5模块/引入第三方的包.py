# 第一 查看 pip 版本  pip -V


# 安装    Pillow  -->  pip install Pillow


# 使用 Pilow 处理图片的一个工具


from PIL import Image

# 打开图片
img = Image.open("2.png");

print(img.format, img.size, img.mode)
