import unittest

from case.identity import indentity
from other.HTMLTestRunner import HTMLTestRunner
from send_email import sendEmail
from test_theme import test_theme
from test_user_action import test_user_action
from test_course_ware import test_course_ware
from test_course import test_course



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_theme))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_user_action))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_course_ware))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_course))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(indentity))

    #

    with open('HTMLReport.html', 'w', encoding='utf8') as f:
        runner = HTMLTestRunner(stream=f,
                                title='鹏云课堂盒子测试',
                                description='鹏云课堂V2.6版本',
                                verbosity=2
                                )
        runner.run(suite)
        # 发送邮件
        authInfo = {}
        authInfo['server'] = 'smtp.163.com'
        authInfo['user'] = 'wangrannet@163.com'
        authInfo['password'] = 'ranrannet'
        fromAdd = 'wangrannet@163.com'
        toAdd = ['943187376@qq.com']
        subject = '鹏云课堂V2.6版本'
        plainText = '鹏云课堂V2.6版本接口测试，详情请下载附件'
        sendEmail(authInfo, fromAdd, toAdd, subject, plainText)