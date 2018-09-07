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
# 插入数据

try:
    cursor.execute("insert into bandcard values(0,500000),(0,600000),(0,400000),(0,700000)")
    #提交事务
    db.commit()
except:
    #如果提交失败 回滚
    db.rollback()
    pass

# 得到执行语句所返回的信息
data = cursor.fetchone()

print(data)

cursor.close()
db.close()
