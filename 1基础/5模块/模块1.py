import sys

#引入系统模块  

# 获取命令行参数的列表
print(sys.argv)

for i in sys.argv:
    print(i)

# name = sys.argv[1]
# age = sys.argv[2]
# num = sys.argv[3]

# print(name, age, num)

# 自动查找所需模块的路径的列表
print(sys.path)
