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

sql = "select version()"

# 执行sql语句
cursor.execute(sql)

# 得到执行语句所返回的信息
data = cursor.fetchone()

print(data)

cursor.close()
db.close()
