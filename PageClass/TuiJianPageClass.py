#!/user/bin/env python
#!encoding=utf-8
import time
from Common.LogTools import LogTools
from Common.ReadYamlTools import ReadYamlTools
from Common.ReadXmlTools import ReadXmlTools
from Common.WebdriverTools import WebdriverTools
from Common.PathTools import image_path

'''推荐模块相关流程操作封装函数'''

class TuiJianPageClass:
    def __init__(self):
        '''初始化'''
        self.yamltool = ReadYamlTools('TuiJianPage.yaml')
        self.xmltool = ReadXmlTools()
        self.log = LogTools()
        self.driver = WebdriverTools()
        self.TJ_eleloc = self.yamltool.get_yaml_section_items('TuiJianPage','TJ')
        self.ESJY_eleloc=self.yamltool.get_yaml_section_items('TuiJianPage','ESJY')
        self.FEGM_eleloc=self.yamltool.get_yaml_section_items('TuiJianPage','FEGM')
        self.GMFS_eleloc=self.yamltool.get_yaml_section_items('TuiJianPage','GMFS')
        self.GMPL_eleloc=self.yamltool.get_yaml_section_items('TuiJianPage','GMPL')
        self.datas = self.xmltool.get_childs_items('TuiJianPage')

    def action_goto_esjy(self):
        '''二手交易专区--二手交易--二手交易评论'''
        self.log.info('[action_start]二手交易评论操作执行开始')
        try:
            #进入二手交易专区
            self.driver.wait_for_one_of_eles(self.TJ_eleloc['element_ershoudeal'],1,10)
            self.driver.one_of_elements_click(self.TJ_eleloc['element_ershoudeal'],1)
            self.driver.wait_for_element(self.ESJY_eleloc['element_esjy_title'],5)
            self.log.info('[action]进入二手交易专区成功')
            #进入二手相关交易
            self.driver.one_of_elements_click(self.ESJY_eleloc['elements_esjy_deal'],0)
            self.driver.wait_for_element(self.ESJY_eleloc['element_deal_gameattr'],5)
            self.log.info('[action]选择的二手交易成功')
            #二手交易评论
            self.driver.element_click(self.ESJY_eleloc['element_deal_pl'])
            self.driver.wait_for_element(self.ESJY_eleloc['element_deal_pl_input'],5)
            self.log.info('[action]进入二手交易评论模块成功')
            self.driver.element_click(self.ESJY_eleloc['element_deal_pl_input'])
            self.driver.element_sendkeys(self.ESJY_eleloc['element_deal_pl_input'],self.datas['esjy_pl'])
            time.sleep(2)
            self.driver.element_click(self.ESJY_eleloc['element_deal_pl_ok'])
            self.driver.wait_for_element(self.ESJY_eleloc['element_deal_gameattr'],5)
            self.log.info('[action]二手交易评论成功，评论内容为【{}】'.format(self.datas['esjy_pl']))
            self.log.info('[action]即将返回主页')
            #返回主页
            self.driver.element_click(self.ESJY_eleloc['element_deal_goback'])
            time.sleep(2)
            self.driver.wait_for_element(self.ESJY_eleloc['element_esjy_title'],5)
            self.driver.element_click(self.ESJY_eleloc['element_esjy_goback'])
            time.sleep(2)
            self.driver.wait_for_element(self.TJ_eleloc['element_tj_title'],5)
            self.log.info('[action]返回主页成功')
            self.log.info('[action_result]二手交易评论操作执行成功')
            self.log.info('[action_end]二手交易评论操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]二手交易评论操作执行失败')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('二手交易评论失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_goto_freegame(self):
        '''PS+会员免费游戏评论'''
        self.log.info('[action_start]PS+会员免费游戏评论操作执行开始')
        try:
            #进入PS+会员免费游戏新闻
            self.driver.wait_for_one_of_eles(self.TJ_eleloc['element_freegame'],2,10)
            self.driver.one_of_elements_click(self.TJ_eleloc['element_freegame'],2)
            self.driver.wait_for_element(self.FEGM_eleloc['element_gamenews'],5)
            self.log.info('[action]进入PS+会员免费游戏新闻成功')
            #点击评论模块
            self.driver.element_click(self.FEGM_eleloc['element_gamenews_pl'])
            self.driver.wait_for_element(self.FEGM_eleloc['element_pl_title'],5)
            self.log.info('[action]进入评论模块成功')
            #发表评论
            self.driver.element_click(self.FEGM_eleloc['element_pl_door'])
            self.driver.wait_for_element(self.FEGM_eleloc['element_pl_input'],5)
            self.log.info('[action]即将发表评论')
            self.driver.element_click(self.FEGM_eleloc['element_pl_input'])
            self.driver.element_sendkeys(self.FEGM_eleloc['element_pl_input'],self.datas['fegm_pl'])
            self.driver.element_click(self.FEGM_eleloc['element_pl_ok'])
            self.driver.wait_for_one_of_eles(self.FEGM_eleloc['element_pl_text'],0,5)
            self.log.info('[action]评论成功，评论内容为{}'.format(self.datas['fegm_pl']))
            self.log.info('[action]即将返回主页')
            #返回主页
            self.driver.element_click(self.FEGM_eleloc['element_pl_goback'])
            self.driver.wait_for_element(self.FEGM_eleloc['element_gamenews_pl'],5)
            self.driver.element_click(self.FEGM_eleloc['element_gamenews_goback'])
            self.driver.wait_for_element(self.TJ_eleloc['element_tj_title'],5)
            self.log.info('[action_result]PS+会员免费游戏评论操作执行成功')
            self.log.info('[aciton_end]PS+会员免费游戏评论操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]PS+会员免费游戏评论操作执行失败')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('PS+会员免费游戏评论失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_goto_gamelist(self):
        '''游戏发售表分享并取消'''
        self.log.info('[action_start]游戏发售表操作执行开始')
        try:
            #进入游戏发售表
            self.driver.wait_for_one_of_eles(self.TJ_eleloc['element_gamelist'],3,10)
            self.driver.one_of_elements_click(self.TJ_eleloc['element_gamelist'],3)
            self.driver.wait_for_element(self.GMFS_eleloc['element_gmfs_title'],5)
            self.log.info('[action]进入游戏发售表成功')
            #游戏发售表分享并取消
            self.driver.wait_for_element(self.GMFS_eleloc['element_gmfs_fx'],5)
            self.driver.element_click(self.GMFS_eleloc['element_gmfs_fx'])
            self.driver.wait_for_element(self.GMFS_eleloc['element_fx_cancle'],5)
            self.log.info('[action]发售表分享打开成功')
            self.driver.element_click(self.GMFS_eleloc['element_fx_cancle'])
            self.driver.wait_for_element(self.GMFS_eleloc['element_gmfs_title'],5)
            self.log.info('[action]发售表分享并取消')
            #返回主页
            self.log.info('[action]即将返回主页')
            self.driver.element_click(self.GMFS_eleloc['element_gmfs_goback'])
            self.driver.wait_for_element(self.TJ_eleloc['element_tj_title'],5)
            self.log.info('[action_result]游戏发售表操作执行成功')
            self.log.info('[aciton_end]游戏发售表操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]游戏发售表操作执行失败')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('游戏发售表操作失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_goto_gamenews(self):
        '''游戏新闻发表评论'''
        self.log.info('[action_start]游戏新闻发表评论操作执行开始')
        try:
            # 进入游戏新闻
            self.driver.wait_for_one_of_eles(self.GMPL_eleloc['elements_newslist'],1,10)
            self.driver.one_of_elements_click(self.GMPL_eleloc['elements_newslist'],1)
            self.driver.wait_for_element(self.GMPL_eleloc['element_news_pl'],5)
            self.log.info('[action]进入游戏新闻成功')
            #点击评论
            self.driver.element_click(self.GMPL_eleloc['element_news_pl'])
            self.driver.wait_for_element(self.GMPL_eleloc['element_pl_input'],5)
            self.log.info('[aciton]开始发表评论')
            #编辑评论并发送
            self.driver.element_click(self.GMPL_eleloc['element_pl_input'])
            self.driver.element_sendkeys(self.GMPL_eleloc['element_pl_input'],self.datas['gmpl_pl'])
            self.driver.element_click(self.GMPL_eleloc['element_pl_ok'])
            self.driver.wait_for_element(self.GMPL_eleloc['element_news_pl'],5)
            self.log.info('[action]评论发表成功，评论内容为【{}】'.format(self.datas['gmpl_pl']))
            self.log.info('[action]即将返回主页')
            #返回主页
            self.driver.element_click(self.GMPL_eleloc['element_news_goback'])
            self.driver.wait_for_element(self.TJ_eleloc['element_tj_title'], 5)
            self.log.info('[action_result]游戏新闻发表评论操作执行成功')
            self.log.info('[aciton_end]游戏新闻发表评论操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]游戏新闻发表评论操作执行失败')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('游戏新闻发表评论失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def quitDriver(self):
        self.driver.quitDriver()

if __name__=="__main__":
    tuijianpage=TuiJianPageClass()
    # tuijianpage.action_goto_esjy()
    # tuijianpage.action_goto_freegame()
    # tuijianpage.action_goto_gamelist()
    tuijianpage.action_goto_gamenews()
