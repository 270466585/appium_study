#!/user/bin/env python
#!encoding=utf-8
import unittest
from PageClass.LoginPageClass import LoginPageClass

'''A9VG一般登录&注销流程自动化测试'''

class LoginCaseTest(unittest.TestCase):
    '''A9VG一般登录&注销流程自动化测试'''
    def setUp(self):
        self.driver=LoginPageClass()

    def tearDown(self):
        self.driver.quitDriver()

    def test_001_login(self):
        '''登录&注销流程:APP一般登录&注销流程'''
        self.driver.action_login()
        self.driver.action_goback_shouye()
        self.driver.action_logout()

if __name__=="__main__":
    unittest.main()




