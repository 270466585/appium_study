#!/user/bin/env python
#!encoding=utf-8
import unittest
from PageClass.FaXianPageClass import FaXianPageClass

'''A9VG发现模块流程自动化测试'''

class FaXianCaseTest(unittest.TestCase):
    '''A9VG发现模块流程自动化测试'''
    @classmethod
    def setUpClass(self):
        self.driver=FaXianPageClass()

    @classmethod
    def tearDownClass(self):
        self.driver.quitDriver()

    def test_001_fjjy(self):
        '''发现模块-添加附近机友'''
        self.driver.action_add_fjjy()

    def test_002_psjb_sj(self):
        '''发现模块-ps奖杯-时间'''
        self.driver.action_psjb_sj()

    def test_003_psjb_fs(self):
        '''发现模块-ps奖杯-分数'''
        self.driver.action_psjb_fs()

    def test_004_psjb_wjs(self):
        '''发现模块-ps奖杯-玩家数'''
        self.driver.action_psjb_wjs()

    def test_005_psjb_nd(self):
        '''发现模块-ps奖杯-难度'''
        self.driver.action_psjb_nd()

    def test_006_psph_dj(self):
        '''发现模块-ps排行-等级'''
        self.driver.action_psph_dj()

    def test_007_psph_jbs(self):
        '''发现模块-ps排行-奖杯数'''
        self.driver.action_psph_jbs()

    def test_008_psph_yxs(self):
        '''发现模块-ps排行-游戏数'''
        self.driver.action_psph_yxs()

    def test_009_psph_wms(self):
        '''发现模块-ps排行-完美数'''
        self.driver.action_psph_wms()

if __name__=="__main__":
    unittest.main()