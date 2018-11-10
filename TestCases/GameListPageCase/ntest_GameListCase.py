#!/user/bin/env python
#!encoding=utf-8
import unittest
from PageClass.GameListPageClass import GameListPageClass

'''A9VG游戏库相关流程自动化测试'''

class GameListCaseTest(unittest.TestCase):
    '''A9VG游戏库相关流程自动化测试'''
    @classmethod
    def setUpClass(self):
        self.driver=GameListPageClass()

    @classmethod
    def tearDownClass(self):
        self.driver.quitDriver()

    def test_001_jjfs(self):
        '''游戏库-即将发售'''
        self.driver.action_jjfs()

    def test_002_bzrm(self):
        '''游戏库-本周热门'''
        self.driver.action_bzrm()

if __name__=="__main__":
    unittest.main()