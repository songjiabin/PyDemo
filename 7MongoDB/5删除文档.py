# pip install pymongo 安装

from pymongo import MongoClient
from  bson.objectid import ObjectId
import pymongo



# 删除文档

# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库 数据库的名字是 myDB
db = conn.myDB

# 得到数据库下面的集合
colletion = db.student


#开始操作数控下面的 表（colletion）

# 删除文档  删除文档中 name 为 tom1 的数据
res = colletion.remove({"name":"tom1"})

# 全部删除
# colletion.remove()


print(res)











conn.close()