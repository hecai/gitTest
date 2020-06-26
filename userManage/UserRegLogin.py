# coding:utf-8
# 导入pymysql驱动
import pymysql
import warnings


# 定义类user_manage
class user_manage:
    # 初始化 传入两个参数：用户名和密码
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    # 执行select SQL语句并返回结果
    def execQuerySql(self, sql, arg):
        db = pymysql.connect(host="127.0.0.1", user='root', database='ums', password='921226hs')
        cursor = db.cursor()
        cursor.execute(sql, [arg])
        try:
            val = cursor.fetchone()[0]
            return val
        except Exception as e:
            print(e)
        finally:
            db.close()


    # 执行insert语句
    def execUpdateSql(self, sql, args):
        warnings.simplefilter("ignore", Warning)
        conn = pymysql.connect(host="127.0.0.1", user='root', database='ums', password='921226hs')
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
        conn.close

    # 判断用户是否存在
    def userIsExist(self):
        sql1 = '''select count(*) from user_info where status='active' and name = %s'''
        userCount = self.execQuerySql(sql1, self.name)
        if userCount:
            return False
        else:
            return True

    # 用户注册
    def userReg(self):
        lenFlag = 6 <= len(self.passwd) <= 10
        # 判断是否存在同名用户
        if self.userIsExist():
            # 判断密码长度是否符合要求
            if lenFlag:
                sql2 = '''insert into user_info values (null,%s,%s,'active');'''
                # self.cursor.execute(sql2,[self.name,self.passwd])
                # self.conn.commit()
                args = [self.name, self.passwd]
                self.execUpdateSql(sql2, args)
                return "regSuccess"
            else:
                return "passwordLenError"
        else:
            return "SameNameError"

    def isActive(self):
        sql3 = '''select status from user_info where  name=%s;'''
        ustatus = self.execQuerySql(sql3, self.name)
        if ustatus == "active":
            return True
        else:
            return False

    # 用户登录
    def userLogin(self):
        '''
        用户状态为active则校验密码是否正确
        反之则抛出异常
        '''
        if self.isActive():
            sql4 = '''select password from user_info where name=%s and status="active";'''
            pwdInDB = self.execQuerySql(sql4, self.name)
            if self.passwd == pwdInDB:
                return "loginSuccess"
            else:
                return "passwordError"
        else:
            return "UserStatusError"

    # 删除用户
    def deleteUser(self, arg):
        sql = '''delete from user_info where name=%s'''
        db = pymysql.connect(host="127.0.0.1", user='root', database='ums', password='921226hs')
        cursor = db.cursor()
        cursor.execute(sql, [arg])
        print(cursor.rowcount)
        db.commit()
        db.close()




if __name__ == '__main__':
    # 实例化
    user1 = user_manage("TestUser2", "1234User2")
    user1.userReg()
