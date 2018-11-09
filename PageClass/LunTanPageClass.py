#!/user/bin/env python
#!encoding=utf-8
import time
from Common.LogTools import LogTools
from Common.ReadYamlTools import ReadYamlTools
from Common.ReadXmlTools import ReadXmlTools
from Common.WebdriverTools import WebdriverTools
from Common.PathTools import image_path

'''论坛模块相关流程操作封装函数'''

class LunTanPageClass:
    def __init__(self):
        '''初始化'''
        self.yamltool = ReadYamlTools('LunTanPage.yaml')
        self.xmltool = ReadXmlTools()
        self.log = LogTools()
        self.driver = WebdriverTools()
        self.LT_eleloc = self.yamltool.get_yaml_section_items('LunTanPage', 'LT')
        self.ZHHF_eleloc = self.yamltool.get_yaml_section_items('LunTanPage', 'ZHHF')
        self.ZXFB_eleloc = self.yamltool.get_yaml_section_items('LunTanPage', 'ZXFB')
        self.JHT_eleloc = self.yamltool.get_yaml_section_items('LunTanPage', 'JHT')
        self.ZDT_eleloc = self.yamltool.get_yaml_section_items('LunTanPage', 'ZDT')
        self.datas = self.xmltool.get_childs_items('LunTanPage')

    def action_pl_zhhf(self):
        '''论坛模块-最后回复帖子评论'''
        self.log.info('[action_start]论坛模块最后回复帖子评论操作执行开始')
        try:
            #进入论坛模块
            self.driver.wait_for_element(self.LT_eleloc['element_lt'],10)
            self.driver.element_click(self.LT_eleloc['element_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'],10)
            self.log.info('[action]进入论坛模块成功')
            #进入Switch综合讨论专区
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt'],10)
            self.driver.element_click(self.LT_eleloc['element_ns_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'],10)
            self.log.info('[action]进入Switch综合讨论专区成功')
            #进入最后回复模块
            self.driver.element_click(self.LT_eleloc['element_ns_zhhf'])
            self.driver.wait_for_one_of_eles(self.ZHHF_eleloc['elements_zhhf_list'], 2, 10)
            self.driver.one_of_elements_click(self.ZHHF_eleloc['elements_zhhf_list'],2)
            self.driver.wait_for_element(self.ZHHF_eleloc['element_zhhf_dxck'],10)
            self.log.info('[action]进入最后回复模块帖子成功')
            #发表评论
            self.driver.wait_for_element(self.ZHHF_eleloc['element_zhhf_fbhf'],10)
            self.driver.element_click(self.ZHHF_eleloc['element_zhhf_fbhf'])
            self.driver.wait_for_element(self.ZHHF_eleloc['element_zhhf_hf'],10)
            self.driver.element_click(self.ZHHF_eleloc['element_zhhf_hf'])
            self.driver.element_sendkeys(self.ZHHF_eleloc['element_zhhf_hf'],self.datas['zhhf_pl'])
            self.driver.element_click(self.ZHHF_eleloc['element_zhhf_hf_ok'])
            self.driver.wait_for_element(self.ZHHF_eleloc['element_zhhf_zklz'],10)
            self.log.info('[action]最后回复模块帖子评论成功，评论内容为【{}】'.format(self.datas['zhhf_pl']))
            self.log.info('[action]即将返回论坛')
            #返回论坛
            self.driver.element_click(self.ZHHF_eleloc['element_zhhf_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'],10)
            self.driver.element_click(self.LT_eleloc['element_ns_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'],10)
            self.log.info('[action]返回论坛成功')
            self.log.info('[action_result]论坛模块最后回复帖子评论执行成功')
            self.log.info('[action_end]论坛模块最后回复帖子评论执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]论坛模块最后回复帖子评论执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('论坛最后回复帖子评论执行')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_pl_zxfb(self):
        '''论坛模块-最新发布帖子评论'''
        self.log.info('[action_start]论坛模块最新发布帖子评论操作执行开始')
        try:
            #进入论坛模块
            self.driver.wait_for_element(self.LT_eleloc['element_lt'], 10)
            self.driver.element_click(self.LT_eleloc['element_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'], 10)
            self.log.info('[action]进入论坛模块成功')
            #进入Switch综合讨论专区
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt'], 10)
            self.driver.element_click(self.LT_eleloc['element_ns_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'], 10)
            self.log.info('[action]进入Switch综合讨论专区成功')
            #进入最新发布模块
            self.driver.element_click(self.LT_eleloc['element_ns_zxfb'])
            self.driver.wait_for_one_of_eles(self.ZXFB_eleloc['elements_zxfb_list'],2,10)
            self.driver.one_of_elements_click(self.ZXFB_eleloc['elements_zxfb_list'],2)
            self.driver.wait_for_element(self.ZXFB_eleloc['element_zxfb_dxck'],10)
            self.log.info('[action]进入最新发布模块帖子成功')
            #发表评论
            self.driver.wait_for_element(self.ZXFB_eleloc['element_zxfb_fbhf'],10)
            self.driver.element_click(self.ZXFB_eleloc['element_zxfb_fbhf'])
            self.driver.wait_for_element(self.ZXFB_eleloc['element_zxfb_hf'],10)
            self.driver.element_click(self.ZXFB_eleloc['element_zxfb_hf'])
            self.driver.element_sendkeys(self.ZXFB_eleloc['element_zxfb_hf'],self.datas['zxfb_pl'])
            self.driver.element_click(self.ZXFB_eleloc['element_zxfb_hf_ok'])
            self.driver.wait_for_element(self.ZXFB_eleloc['element_zxfb_zklz'],10)
            self.log.info('[action]最新发布模块帖子评论成功，评论内容为【{}】'.format(self.datas['zxfb_pl']))
            self.log.info('[action]即将返回论坛')
            #返回论坛
            self.driver.element_click(self.ZXFB_eleloc['element_zxfb_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'], 10)
            self.driver.element_click(self.LT_eleloc['element_ns_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'], 10)
            self.log.info('[action]返回论坛成功')
            self.log.info('[action_result]论坛模块最新发布帖子评论执行成功')
            self.log.info('[action_end]论坛模块最新发布帖子评论执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]论坛模块最新发布帖子评论执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('论坛最新发布帖子评论执行')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_pl_jht(self):
        '''论坛模块-精华帖帖子评论'''
        self.log.info('[action_start]论坛模块精华帖帖子评论操作执行开始')
        try:
            #进入论坛模块
            self.driver.wait_for_element(self.LT_eleloc['element_lt'], 10)
            self.driver.element_click(self.LT_eleloc['element_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'], 10)
            self.log.info('[action]进入论坛模块成功')
            #进入Switch综合讨论专区
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt'], 10)
            self.driver.element_click(self.LT_eleloc['element_ns_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'], 10)
            self.log.info('[action]进入Switch综合讨论专区成功')
            #进入精华帖模块
            self.driver.element_click(self.LT_eleloc['element_ns_jht'])
            self.driver.wait_for_one_of_eles(self.JHT_eleloc['elements_jht_list'], 1, 10)
            self.driver.one_of_elements_click(self.JHT_eleloc['elements_jht_list'],1)
            self.driver.wait_for_element(self.JHT_eleloc['element_jht_dxck'],10)
            self.log.info('[action]进入精华帖模块帖子成功')
            #发表评论
            self.driver.wait_for_element(self.JHT_eleloc['element_jht_fbhf'],10)
            self.driver.element_click(self.JHT_eleloc['element_jht_fbhf'])
            self.driver.wait_for_element(self.JHT_eleloc['element_jht_hf'],10)
            self.driver.element_click(self.JHT_eleloc['element_jht_hf'])
            self.driver.element_sendkeys(self.JHT_eleloc['element_jht_hf'],self.datas['jht_pl'])
            self.driver.element_click(self.JHT_eleloc['element_jht_hf_ok'])
            self.driver.wait_for_element(self.JHT_eleloc['element_jht_zklz'],10)
            self.log.info('[action]精华帖模块帖子评论成功，评论内容为【{}】'.format(self.datas['jht_pl']))
            self.log.info('[action]即将返回论坛')
            #返回论坛
            self.driver.element_click(self.JHT_eleloc['element_jht_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'], 10)
            self.driver.element_click(self.LT_eleloc['element_ns_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'], 10)
            self.log.info('[action]返回论坛成功')
            self.log.info('[action_result]论坛模块精华帖帖子评论执行成功')
            self.log.info('[action_end]论坛模块精华帖帖子评论执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]论坛模块精华帖帖子评论执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('论坛精华帖帖子评论执行')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_pl_zdt(self):
        '''论坛模块-置顶帖帖子评论'''
        self.log.info('[action_start]论坛模块置顶帖帖子评论操作执行开始')
        try:
            #进入论坛模块
            self.driver.wait_for_element(self.LT_eleloc['element_lt'], 10)
            self.driver.element_click(self.LT_eleloc['element_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'], 10)
            self.log.info('[action]进入论坛模块成功')
            #进入Switch综合讨论专区
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt'], 10)
            self.driver.element_click(self.LT_eleloc['element_ns_lt'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'], 10)
            self.log.info('[action]进入Switch综合讨论专区成功')
            #进入置顶帖模块
            self.driver.element_click(self.LT_eleloc['element_ns_zdt'])
            self.driver.wait_for_one_of_eles(self.ZDT_eleloc['elements_zdt_list'], 5, 10)
            self.driver.one_of_elements_click(self.ZDT_eleloc['elements_zdt_list'],5)
            self.driver.wait_for_element(self.ZDT_eleloc['element_zdt_dxck'],10)
            self.log.info('[action]进入置顶帖模块帖子成功')
            #发表评论
            self.driver.wait_for_element(self.ZDT_eleloc['element_zdt_fbhf'],10)
            self.driver.element_click(self.ZDT_eleloc['element_zdt_fbhf'])
            self.driver.wait_for_element(self.ZDT_eleloc['element_zdt_hf'],10)
            self.driver.element_click(self.ZDT_eleloc['element_zdt_hf'])
            self.driver.element_sendkeys(self.ZDT_eleloc['element_zdt_hf'],self.datas['zdt_pl'])
            self.driver.element_click(self.ZDT_eleloc['element_zdt_hf_ok'])
            self.driver.wait_for_element(self.ZDT_eleloc['element_zdt_zklz'],10)
            self.log.info('[action]置顶帖模块帖子评论成功，评论内容为【{}】'.format(self.datas['zdt_pl']))
            self.log.info('[action]即将返回论坛')
            #返回论坛
            self.driver.element_click(self.ZDT_eleloc['element_jht_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_ns_lt_title'], 10)
            self.driver.element_click(self.LT_eleloc['element_ns_goback'])
            self.driver.wait_for_element(self.LT_eleloc['element_lt_title'], 10)
            self.log.info('[action]返回论坛成功')
            self.log.info('[action_result]论坛模块置顶帖子评论执行成功')
            self.log.info('[action_end]论坛模块置顶帖子评论执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]论坛模块置顶帖子评论执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('论坛置顶帖子评论执行')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def quitDriver(self):
        self.driver.quitDriver()

if __name__=="__main__":
    luntanpage=LunTanPageClass()
    # luntanpage.action_pl_zhhf()
    luntanpage.action_pl_zxfb()
    # luntanpage.action_pl_jht()
    # luntanpage.action_pl_zdt()
