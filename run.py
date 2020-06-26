import unittest

from HTMLTestRunner import HTMLTestRunner
from testCases.UserLoginTest import loginTest
from testCases.UserRegTest import regTest
from util.sendEmail import sendEmail

def suite():
    suite = unittest.TestSuite()
    suite.addTest(loginTest("test_pwdCorrect"))
    suite.addTest(regTest("test_duplicate"))
    suite.addTest(regTest("test_normalPwdLenth"))
    return suite


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
    with open("./TestReport.html", "wb") as f:
        runner = HTMLTestRunner(stream=f, title="Reg and Login Test Report")
        result = runner.run(suite())
        totalNums = suite().countTestCases()
        passedNums = result.success_count
        failedNums = result.failure_count
        skippedNums = len(result.skipped)
        # 通过率，保留两位小数
        passRate = round(passedNums * 100 / totalNums)
        emailBody = '''Hi,all:
                    本次构建一共运行：{totalNums}个用例，通过{passedNums}个，失败{failedNums}个，跳过{skippedNums}个。通过率：{passRate}%.
                    详细信息请查看附件。'''
        content = emailBody.format(totalNums=totalNums, passedNums=passedNums, failedNums=failedNums,
                                   skippedNums=skippedNums, passRate=passRate)
        # 收件人列表
        receiver = ['851641357@qq.com']
        # 测试报告的路径
        path1 = "/Users/hesi/Desktop/unitTest/TestReport.html"
        subject = "登录注册功能每日构建"
        e = sendEmail(subject, content, receiver, attachPath=path1)
        # 发送邮件
        e.sendEmail()