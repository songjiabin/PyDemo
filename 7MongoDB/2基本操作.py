# pip install pymongo 安装

from pymongo import MongoClient

# 添加文档

# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库 数据库的名字是 myDB
db = conn.myDB

# 得到数据库下面的集合
colletion = db.student


#开始操作数控下面的 表（colletion）

# 添加文档

colletion.insert({"name":"tom","age":18,"gender":1,"address":"河北衡水","isDelete":0})

# 添加文档 多个数据

colletion.insert([{"name":"tom","age":18,"gender":1,"address":"河北衡水","isDelete":0},
                  {"name": "tom1", "age": 25, "gender": 1, "address": "河北衡水", "isDelete": 1}])

conn.close()