#!/user/bin/env python
#!encoding=utf-8
import unittest
from PageClass.TuiJianPageClass import TuiJianPageClass

'''A9VG推荐模块流程自动化测试'''

class TuiJianCaseTest(unittest.TestCase):
    '''A9VG推荐模块流程自动化测试'''
    @classmethod
    def setUpClass(self):
        self.driver=TuiJianPageClass()

    @classmethod
    def tearDownClass(self):
        self.driver.quitDriver()

    def test_001_esjy(self):
        '''推荐模块-二手交易流程自动化测试'''
        self.driver.action_goto_esjy()

    def test_002_freegame(self):
        '''推荐模块-PS+会员免费游戏流程自动化测试'''
        self.driver.action_goto_freegame()

    def test_003_gamelist(self):
        '''推荐模块-游戏发售表流程自动化测试'''
        self.driver.action_goto_gamelist()

    def test_004_gamenews(self):
        '''推荐模块-游戏新闻流程自动化测试'''
        self.driver.action_goto_gamenews()

if __name__=="__main__":
    unittest.main()