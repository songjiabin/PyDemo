import pickle

dataList = [1, 2, 3, "我是基本密码"]

# 写 将数据存储到 txt中
path = r"E:\py_project_path\持久化.txt"
f = open(path, "wb")
pickle.dump(dataList, f)

f.close()

# 读  持久化的数据

f2 = open(path, "rb");
content = pickle.load(f2)
print(content)
f2.close()
