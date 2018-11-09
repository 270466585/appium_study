#!/user/bin/env python
#!encoding=utf-8
import unittest
from PageClass.LunTanPageClass import LunTanPageClass

'''A9VG论坛模块流程自动化测试'''

class LunTanCaseTest(unittest.TestCase):
    '''A9VG论坛模块流程自动化测试'''
    @classmethod
    def setUpClass(self):
        self.driver=LunTanPageClass()

    @classmethod
    def tearDownClass(self):
        self.driver.quitDriver()

    def test_001_zhhf(self):
        '''论坛模块-最后回复流程自动化测试'''
        self.driver.action_pl_zhhf()

    def test_002_zxfb(self):
        '''论坛模块-最新发布流程自动化测试'''
        self.driver.action_pl_zxfb()

    def test_003_jht(self):
        '''论坛模块-精华帖流程自动化测试'''
        self.driver.action_pl_jht()

    def test_004_zdt(self):
        '''论坛模块-置顶帖流程自动化测试'''
        self.driver.action_pl_zdt()

if __name__=="__main__":
    unittest.main()
