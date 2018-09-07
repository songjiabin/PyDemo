import pymysql


class CommomSql(object):

    def __init__(self, host, user, pwd, dbName):
        self.host = host
        self.user = user
        self.pwd = pwd
        # 连接哪个数据库
        self.dbName = dbName
        pass

    def connet(self):
        self.db = pymysql.connect(self.host, self.user, self.pwd, self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.colse()
        self.db.close()

    def get_one(self, sql):
        result = None
        try:
            # 先连接数据库
            self.connet()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
            pass
        except:
            print("查询失败")

        return result

    def get_all(self, sql):
        result = None
        try:
            # 先连接数据库
            self.connet()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            pass
        except:
            print("查询失败")

        return result

    def insert(self, sql):
        self.__edit(sql)
        pass

    def update(self, sql):
        self.__edit(sql)
        pass

    def delete(self, sql):
        self.__edit(sql)
        pass

    def __edit(self, sql):
        # 影响了多少行
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
            pass
        except:
            print("提交事务失败")
            self.db.rollback()
            pass
        return count
