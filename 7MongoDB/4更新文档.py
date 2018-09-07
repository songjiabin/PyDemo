# pip install pymongo 安装

from pymongo import MongoClient
from  bson.objectid import ObjectId
import pymongo



# 更新文档

# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库 数据库的名字是 myDB
db = conn.myDB

# 得到数据库下面的集合
colletion = db.student


#开始操作数控下面的 表（colletion）

# 更新文档
#将 name = 基本密码 的数据  中的 age 变为  88
res = colletion.update({"name":"基本密码"},{"$set":{"age":88}})

print(res)











conn.close()