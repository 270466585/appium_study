#!/user/bin/env python
#!encoding=utf-8
import time
from Common.LogTools import LogTools
from Common.ReadYamlTools import ReadYamlTools
from Common.ReadXmlTools import ReadXmlTools
from Common.WebdriverTools import WebdriverTools
from Common.PathTools import image_path

'''游戏库相关流程操作封装函数'''

class GameListPageClass:
    def __init__(self):
        '''初始化'''
        self.yamltool = ReadYamlTools('GameListPage.yaml')
        self.xmltool = ReadXmlTools()
        self.log = LogTools()
        self.driver = WebdriverTools()
        self.GL_eleloc = self.yamltool.get_yaml_section_items('GameListPage', 'GL')
        self.JJFS_eleloc = self.yamltool.get_yaml_section_items('GameListPage', 'JJFS')
        self.BZRM_eleloc = self.yamltool.get_yaml_section_items('GameListPage', 'BZRM')
        self.datas = self.xmltool.get_childs_items('GameListPage')

    def action_jjfs(self):
        '''游戏库-即将发售相关操作'''
        self.log.info('[action_start]游戏库即将发售相关操作执行开始')
        try:
            #进入游戏库
            self.driver.wait_for_element(self.GL_eleloc['element_gl'],10)
            self.driver.element_click(self.GL_eleloc['element_gl'])
            self.driver.wait_for_element(self.GL_eleloc['element_gl_title'],10)
            self.log.info('[action]进入游戏库成功')
            #进入即将发售游戏信息
            self.driver.wait_for_one_of_eles(self.GL_eleloc['elements_gl_jjfs_list'],6,10)
            self.driver.one_of_elements_click(self.GL_eleloc['elements_gl_jjfs_list'],6)
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_gm_title'],10)
            self.log.info('[action]进入即将发售游戏信息成功')
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_gm_sc'])
            time.sleep(2)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_gm_xxkz'])
            time.sleep(5)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_gm_xskz'])
            #游戏评论
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_gm_pl'])
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_pl_title'],10)
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_pl_dp'],10)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_pl_dp'])
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_dp_title'],10)
            self.log.info('[action]进入即将发售游戏写点评界面成功')
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_dp_xw'],10)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_dp_xw'])
            time.sleep(2)
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_dp_pt_ps4'], 10)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_dp_pt_ps4'])
            time.sleep(2)
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_dp_input'],10)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_dp_input'])
            self.driver.element_sendkeys(self.JJFS_eleloc['element_jjfs_dp_input'],self.datas['jjfs_pl'])
            time.sleep(2)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_dp_fbpl'])
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_gm_title'],10)
            self.log.info('[action]即将发售游戏评论成功，内容为{}'.format(self.datas['jjfs_pl']))
            self.log.info('[action]即将返回游戏库')
            #返回游戏库
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_gm_goback'],10)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_gm_goback'])
            self.driver.wait_for_element(self.JJFS_eleloc['element_jjfs_gm_title'],10)
            self.driver.element_click(self.JJFS_eleloc['element_jjfs_gm_goback'])
            self.driver.wait_for_element(self.GL_eleloc['element_gl_title'],10)
            self.log.info('[action]返回游戏库成功')
            self.log.info('[action_result]游戏库即将发售相关操作执行成功')
            self.log.info('[action_end]游戏库即将发售相关操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]游戏库即将发售相关操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('游戏库即将发售操作执行')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_bzrm(self):
        '''游戏库-本周热门相关操作'''
        self.log.info('[action_start]游戏库本周热门相关操作执行开始')
        try:
            # 进入游戏库
            self.driver.wait_for_element(self.GL_eleloc['element_gl'], 20)
            self.driver.element_click(self.GL_eleloc['element_gl'])
            self.driver.wait_for_element(self.GL_eleloc['element_gl_title'], 10)
            self.log.info('[action]进入游戏库成功')
            #进入本周热门游戏
            self.driver.wait_for_one_of_eles(self.GL_eleloc['elements_gl_bzrm_list'],0,10)
            self.driver.one_of_elements_click(self.GL_eleloc['elements_gl_bzrm_list'],0)
            self.driver.wait_for_element(self.BZRM_eleloc['element_bzrm_gm_title'],10)
            self.log.info('[action]进入本周热门游戏信息成功')
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_gm_sc'])
            time.sleep(3)
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_gm_xxkz'])
            time.sleep(3)
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_gm_xskz'])
            #游戏评论
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_gm_pl'])
            self.driver.wait_for_element(self.BZRM_eleloc['element_bzrm_pl_title'],10)
            self.driver.wait_for_element(self.BZRM_eleloc['element_bzrm_pl_dp'], 10)
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_pl_dp'])
            self.driver.wait_for_element(self.BZRM_eleloc['element_bzrm_dp_title'],10)
            self.log.info('[action]进入本周热门游戏写点评界面成功')
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_dp_xw'])
            time.sleep(2)
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_dp_pt_ps4'])
            time.sleep(2)
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_dp_input'])
            self.driver.element_sendkeys(self.BZRM_eleloc['element_bzrm_dp_input'],self.datas['bzrm_pl'])
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_dp_fbpl'])
            self.driver.wait_for_element(self.BZRM_eleloc['element_bzrm_gm_title'],10)
            self.log.info('[action]本周热门游戏评论成功，内容为{}'.format(self.datas['bzrm_pl']))
            self.log.info('[action]即将返回游戏库')
            # 返回游戏库
            self.driver.wait_for_element(self.BZRM_eleloc['element_bzrm_gm_goback'], 10)
            self.driver.element_click(self.BZRM_eleloc['element_bzrm_gm_goback'])
            self.driver.wait_for_element(self.GL_eleloc['element_gl_jjfs'], 10)
            self.log.info('[action]返回游戏库成功')
            self.log.info('[action_result]游戏库本周热门相关操作执行成功')
            self.log.info('[action_end]游戏库本周热门相关操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]游戏库本周热门相关操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('游戏库本周热门操作执行')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def quitDriver(self):
        self.driver.quitDriver()

if __name__=="__main__":
    gamelist=GameListPageClass()
    gamelist.action_jjfs()
    # gamelist.action_bzrm()