import unittest
from userManage.UserRegLogin import user_manage


class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 先注册用户
        cls.user = user_manage("TestUser", "123456hs")
        cls.user.userReg()

    # 判断用户名密码不匹配情况
    def test_pwdCorrect(self):
        user1 = user_manage("TestUser", "123456")
        result = user1.userLogin()
        self.assertEqual(result, "passwordError")

    @classmethod
    def tearDownClass(cls):
        cls.user.deleteUser(["TestUser"])
