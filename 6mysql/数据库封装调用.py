from 数据库操作的封装 import CommomSql

if __name__ == '__main__':
    commomSql = CommomSql("localhost", "root", "", "songjiab")

    sql_select_one = "select * from bandcard where id =3"

    result =commomSql.get_all(sql_select_one)

    print(result)
