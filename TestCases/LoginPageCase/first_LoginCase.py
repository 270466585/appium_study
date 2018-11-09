#!/user/bin/env python
#!encoding=utf-8
import unittest
from PageClass.LoginPageClass import LoginPageClass

'''A9VG首次登录&注销流程自动化测试'''

class FirstLoginCaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = LoginPageClass()

    def tearDown(self):
        self.driver.quitDriver()

    def test_01_fristlogin(self):
        '''登录&注销流程:APP首次登录&注销流程'''
        self.driver.action_first_login()
        self.driver.action_goback_shouye()
        self.driver.action_logout()

if __name__=="__main__":
    unittest.main()