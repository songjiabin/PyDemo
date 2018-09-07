# pip install pyMySQL
import pymysql

# 连接数据库
"""
1、mysql 所在主机ip 
2、用户名
3、密码
4、要连接的具体数据库的名字 
"""
db = pymysql.connect("localhost", "root", "", "songjiab")

# 得到cursor对象
cursor = db.cursor();

# 执行sql语句
# 删除数据

try:
    cursor.execute("select * from  bandcard where id >2")
except:
    # 如果提交失败 回滚
    db.rollback()
    print("查询失败")
    pass

# 得到执行语句所返回的信息
dataList = cursor.fetchall()

for data in dataList:
    print("%d--%d"%(data[0],data[1]))
    pass


cursor.close()
db.close()
