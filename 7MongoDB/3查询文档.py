# pip install pymongo 安装

from pymongo import MongoClient
from  bson.objectid import ObjectId
import pymongo



# 查询文档

# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库 数据库的名字是 myDB
db = conn.myDB

# 得到数据库下面的集合
colletion = db.student


#开始操作数控下面的 表（colletion）

# 查询文档

#查询   年龄  > 18 的 人
res =  colletion.find({"age":{"$gt":18}})

#查询所有的数据
res = colletion.find()


#统计一共查出来多少个
count = colletion.count()
print(count)



#用于 id 查询
res =  colletion.find({"_id":ObjectId("5b8b8a2cfdabd6efbf9b7aa0")})



#排序 升序
res =  colletion.find({"age":{"$gt":18}}).sort("age")




#排序 降序
res =  colletion.find({"age":{"$gt":18}}).sort("age",pymongo.DESCENDING)



#分页  先跳过第一个  拿到前两个
res =  colletion.find().skip(1).limit(2)




for data in res:
    print(data)
    print(data.get("name"))
    #返回的事字典的类型
    pass









conn.close()