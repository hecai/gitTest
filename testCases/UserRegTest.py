# coding:utf-8
import unittest
from userManage.UserRegLogin import user_manage


# 定义测试类，用于继承unitTest。TestCase
class regTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试前的准备工作")
        # 注册TestUser3
        cls.user3 = user_manage("TestUser3", "123456")
        cls.user3.userReg()

    # 测试方法或者测试用例要用test开头
    # 测试场景：姓名重复
    def test_duplicate(self):
        user = user_manage("TestUser3", "123478")
        self.assertEqual(user.userReg(), "SameNameError")

    # 测试场景：密码长度正常注册成功
    def test_normalPwdLenth(self):
        self.user4 = user_manage("TestUser4", "123467")
        self.assertEqual(self.user4.userReg(), "regSuccess")
        self.user4.deleteUser([self.user4.name])

    @classmethod
    # 删除创建的记录
    def tearDownClass(cls):
        print("测试结束清理数据")
        cls.user3.deleteUser([cls.user3.name])
        print("已清除完毕")
