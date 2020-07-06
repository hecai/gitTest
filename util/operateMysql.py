import pymysql
from config.config import dbhost, dbuser, dbpassword


def getValue(sql, dbName):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "921226hs", "school")
    # db = pymysql.connect(dbhost, dbuser, dbpassword, dbName)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    value = cursor.fetchall()
    print(value)
    return value


getValue('select * from class', 'school')

