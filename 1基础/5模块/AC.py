import PIL.Image

# 打开图片
img = PIL.Image.open("2.png");

print(img.format, img.size, img.mode)