#!/user/bin/env python
#!encoding=utf-8
import time
from Common.LogTools import LogTools
from Common.ReadYamlTools import ReadYamlTools
from Common.ReadXmlTools import ReadXmlTools
from Common.WebdriverTools import WebdriverTools
from Common.PathTools import image_path

'''发现模块相关流程操作封装函数'''

class FaXianPageClass:
    def __init__(self):
        '''初始化'''
        self.yamltool = ReadYamlTools('FaXianPage.yaml')
        self.xmltool = ReadXmlTools()
        self.log = LogTools()
        self.driver = WebdriverTools()
        self.FX_eleloc = self.yamltool.get_yaml_section_items('FaXianPage', 'FX')
        self.FJJY_eleloc = self.yamltool.get_yaml_section_items('FaXianPage', 'FJJY')
        self.PSPH_eleloc = self.yamltool.get_yaml_section_items('FaXianPage', 'PSPH')
        self.PSJB_eleloc = self.yamltool.get_yaml_section_items('FaXianPage', 'PSJB')
        self.datas = self.xmltool.get_childs_items('FaXianPage')

    def action_add_fjjy(self):
        '''发现模块-添加附近机友'''
        self.log.info('[action_start]发现模块添加附近机友操作流程执行开始')
        try:
            #进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'],10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]发现模块进入成功')
            #进入找机友
            self.driver.wait_for_element(self.FX_eleloc['element_fx_jy'],10)
            self.driver.element_click(self.FX_eleloc['element_fx_jy'])
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_title'],10)
            self.log.info('[action]找机友模块进入成功')
            #添加机友
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_fjjy'],10)
            self.driver.element_click(self.FJJY_eleloc['element_fjjy_fjjy'])
            time.sleep(2)
            self.driver.one_of_elements_click(self.FJJY_eleloc['elements_fjjy_jy_list'],2)
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_jy_title'],10)
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_jy_add'],10)
            self.driver.element_click(self.FJJY_eleloc['element_fjjy_jy_add'])
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_jy_add_input'],10)
            self.driver.element_click(self.FJJY_eleloc['element_fjjy_jy_add_input'])
            self.driver.element_sendkeys(self.FJJY_eleloc['element_fjjy_jy_add_input'],self.datas['FJJY_pl'])
            self.driver.element_click(self.FJJY_eleloc['element_fjjy_jy_add_ok'])
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_jy_title'],10)
            self.log.info('[action]添加机友请求发送成功，添加机友内容为【{}】'.format(self.datas['FJJY_pl']))
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.FJJY_eleloc['element_fjjy_jy_goback'])
            self.driver.wait_for_element(self.FJJY_eleloc['element_fjjy_title'],10)
            self.driver.element_click(self.FJJY_eleloc['element_fjjy_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块添加附近机友操作流程执行成功')
            self.log.info('[action_end]发现模块添加附近机友操作流程执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块添加附近机友操作流程执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块添加附近机友')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psjb_sj(self):
        '''发现模块-PS奖杯时间分类-评论'''
        self.log.info('[action_start]发现模块PS奖杯时间分类评论流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            #进入ps奖杯
            self.driver.wait_for_element(self.FX_eleloc['element_fx_yxjb'],10)
            self.driver.element_click(self.FX_eleloc['element_fx_yxjb'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.log.info('[action]PSN游戏奖杯模块进入成功')
            #进入时间ps奖杯
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_sj'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_sj'])
            self.driver.wait_for_one_of_eles(self.PSJB_eleloc['elements_jb_gm_list'], 0, 10)
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_list'],0)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.log.info('[action]PSN游戏奖杯模块时间分类模块游戏奖杯进入成功')
            #选择一个奖杯进行评论
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_jblist'],1)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]游戏奖杯详情进入成功')
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl_input'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_input'])
            self.driver.element_sendkeys(self.PSJB_eleloc['element_jb_gm_fbpl_input'],self.datas['PSJB_sj_pl'])
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_ok'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]奖杯评论成功，评论内容为【{}】'.format(self.datas['PSJB_sj_pl']))
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_jbxq_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS奖杯时间分类评论流程执行成功')
            self.log.info('[action_end]发现模块PS奖杯时间分类评论流程执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS奖杯时间分类评论流程执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS奖杯时间分类评论')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psjb_fs(self):
        '''发现模块-PS奖杯分数分类-评论'''
        self.log.info('[action_start]发现模块PS奖杯分数分类评论流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            #进入ps奖杯
            self.driver.wait_for_element(self.FX_eleloc['element_fx_yxjb'],10)
            self.driver.element_click(self.FX_eleloc['element_fx_yxjb'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.log.info('[action]PSN游戏奖杯模块进入成功')
            #进入时间ps奖杯
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_fs'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_fs'])
            self.driver.wait_for_one_of_eles(self.PSJB_eleloc['elements_jb_gm_list'],0,10)
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_list'],0)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.log.info('[action]PSN游戏奖杯模块分数分类模块游戏奖杯进入成功')
            #选择一个奖杯进行评论
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_jblist'],1)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]游戏奖杯详情进入成功')
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl_input'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_input'])
            self.driver.element_sendkeys(self.PSJB_eleloc['element_jb_gm_fbpl_input'],self.datas['PSJB_fs_pl'])
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_ok'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]奖杯评论成功，评论内容为【{}】'.format(self.datas['PSJB_fs_pl']))
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_jbxq_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS奖杯分数分类评论流程执行成功')
            self.log.info('[action_end]发现模块PS奖杯分数分类评论流程执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS奖杯分数分类评论流程执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS奖杯分数分类评论')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psjb_wjs(self):
        '''发现模块-PS奖杯玩家数分类-评论'''
        self.log.info('[action_start]发现模块PS奖杯玩家数分类评论流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            #进入ps奖杯
            self.driver.wait_for_element(self.FX_eleloc['element_fx_yxjb'],10)
            self.driver.element_click(self.FX_eleloc['element_fx_yxjb'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.log.info('[action]PSN游戏奖杯模块进入成功')
            #进入时间ps奖杯
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_wjs'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_wjs'])
            self.driver.wait_for_one_of_eles(self.PSJB_eleloc['elements_jb_gm_list'],0,10)
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_list'],0)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.log.info('[action]PSN游戏奖杯模块玩家数分类模块游戏奖杯进入成功')
            #选择一个奖杯进行评论
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_jblist'],1)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]游戏奖杯详情进入成功')
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl_input'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_input'])
            self.driver.element_sendkeys(self.PSJB_eleloc['element_jb_gm_fbpl_input'],self.datas['PSJB_wjs_pl'])
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_ok'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]奖杯评论成功，评论内容为【{}】'.format(self.datas['PSJB_wjs_pl']))
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_jbxq_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS奖杯玩家数分类评论流程执行成功')
            self.log.info('[action_end]发现模块PS奖杯玩家数分类评论流程执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS奖杯玩家数分类评论流程执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS奖杯玩家数分类评论')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psjb_nd(self):
        '''发现模块-PS奖杯难度分类-评论'''
        self.log.info('[action_start]发现模块PS奖杯难度分类评论流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            #进入ps奖杯
            self.driver.wait_for_element(self.FX_eleloc['element_fx_yxjb'],10)
            self.driver.element_click(self.FX_eleloc['element_fx_yxjb'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.log.info('[action]PSN游戏奖杯模块进入成功')
            #进入时间ps奖杯
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_nd'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_nd'])
            self.driver.wait_for_one_of_eles(self.PSJB_eleloc['elements_jb_gm_list'],0,10)
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_list'],0)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.log.info('[action]PSN游戏奖杯模块难度分类模块游戏奖杯进入成功')
            #选择一个奖杯进行评论
            self.driver.one_of_elements_click(self.PSJB_eleloc['elements_jb_gm_jblist'],1)
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]游戏奖杯详情进入成功')
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_fbpl_input'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_input'])
            self.driver.element_sendkeys(self.PSJB_eleloc['element_jb_gm_fbpl_input'],self.datas['PSJB_nd_pl'])
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_fbpl_ok'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jbxq'],10)
            self.log.info('[action]奖杯评论成功，评论内容为【{}】'.format(self.datas['PSJB_nd_pl']))
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_jbxq_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_gm_jblist_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_gm_goback'])
            self.driver.wait_for_element(self.PSJB_eleloc['element_jb_title'],10)
            self.driver.element_click(self.PSJB_eleloc['element_jb_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS奖杯难度分类评论流程执行成功')
            self.log.info('[action_end]发现模块PS奖杯难度分类评论流程执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS奖杯难度分类评论流程执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS奖杯难度分类评论')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psph_dj(self):
        '''发现模块-PS排行榜-通过等级查看玩家信息'''
        self.log.info('[action_start]发现模块PS排行榜等级分类查看玩家信息流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            # 进入ps排行榜
            self.driver.wait_for_element(self.FX_eleloc['element_fx_ph'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx_ph'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'], 10)
            self.log.info('[action]PS排行榜模块进入成功')
            #进入等级-玩家信息界面
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_dj'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_dj'])
            self.driver.wait_for_one_of_eles(self.PSPH_eleloc['elements_ph_list'],0,10)
            self.driver.one_of_elements_click(self.PSPH_eleloc['elements_ph_list'],0)
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_wj_card'],10)
            time.sleep(8)
            self.log.info('[action]进入排行榜玩家信息界面成功')
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSPH_eleloc['element_ph_wj_goback'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS排行榜等级分类查看玩家信息流程操作执行成功')
            self.log.info('[action_end]发现模块PS排行榜等级分类查看玩家信息流程操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS排行榜等级分类查看玩家信息流程操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS排行榜等级分类查看玩家信息')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psph_jbs(self):
        '''发现模块-PS排行榜-通过奖杯数查看玩家信息'''
        self.log.info('[action_start]发现模块PS排行榜奖杯数分类查看玩家信息流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            # 进入ps排行榜
            self.driver.wait_for_element(self.FX_eleloc['element_fx_ph'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx_ph'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'], 10)
            self.log.info('[action]PS排行榜模块进入成功')
            #进入奖杯数-玩家信息界面
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_jbs'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_jbs'])
            self.driver.wait_for_one_of_eles(self.PSPH_eleloc['elements_ph_list'],0,10)
            self.driver.one_of_elements_click(self.PSPH_eleloc['elements_ph_list'],0)
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_wj_card'],10)
            time.sleep(8)
            self.log.info('[action]进入排行榜玩家信息界面成功')
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSPH_eleloc['element_ph_wj_goback'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS排行榜奖杯数分类查看玩家信息流程操作执行成功')
            self.log.info('[action_end]发现模块PS排行榜奖杯数分类查看玩家信息流程操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS排行榜奖杯数分类查看玩家信息流程操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS排行榜奖杯数分类查看玩家信息')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psph_yxs(self):
        '''发现模块-PS排行榜-通过游戏数查看玩家信息'''
        self.log.info('[action_start]发现模块PS排行榜游戏数分类查看玩家信息流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            # 进入ps排行榜
            self.driver.wait_for_element(self.FX_eleloc['element_fx_ph'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx_ph'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'], 10)
            self.log.info('[action]PS排行榜模块进入成功')
            #进入游戏数-玩家信息界面
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_yxs'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_yxs'])
            self.driver.wait_for_one_of_eles(self.PSPH_eleloc['elements_ph_list'],0,10)
            self.driver.one_of_elements_click(self.PSPH_eleloc['elements_ph_list'],0)
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_wj_card'],10)
            time.sleep(8)
            self.log.info('[action]进入排行榜玩家信息界面成功')
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSPH_eleloc['element_ph_wj_goback'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS排行榜游戏数分类查看玩家信息流程操作执行成功')
            self.log.info('[action_end]发现模块PS排行榜游戏数分类查看玩家信息流程操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS排行榜游戏数分类查看玩家信息流程操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS排行榜游戏数分类查看玩家信息')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_psph_wms(self):
        '''发现模块-PS排行榜-通过完美数查看玩家信息'''
        self.log.info('[action_start]发现模块PS排行榜完美数分类查看玩家信息流程操作执行开始')
        try:
            # 进入发现模块
            self.driver.wait_for_element(self.FX_eleloc['element_fx'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'], 10)
            self.log.info('[action]发现模块进入成功')
            # 进入ps排行榜
            self.driver.wait_for_element(self.FX_eleloc['element_fx_ph'], 10)
            self.driver.element_click(self.FX_eleloc['element_fx_ph'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'], 10)
            self.log.info('[action]PS排行榜模块进入成功')
            #进入完美数-玩家信息界面
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_wms'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_wms'])
            self.driver.wait_for_one_of_eles(self.PSPH_eleloc['elements_ph_list'],0,10)
            self.driver.one_of_elements_click(self.PSPH_eleloc['elements_ph_list'],0)
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_wj_card'],10)
            time.sleep(8)
            self.log.info('[action]进入排行榜玩家信息界面成功')
            self.log.info('[action]即将返回发现模块')
            #返回发现模块
            self.driver.element_click(self.PSPH_eleloc['element_ph_wj_goback'])
            self.driver.wait_for_element(self.PSPH_eleloc['element_ph_title'],10)
            self.driver.element_click(self.PSPH_eleloc['element_ph_goback'])
            self.driver.wait_for_element(self.FX_eleloc['element_fx_title'],10)
            self.log.info('[action]返回发现模块成功')
            self.log.info('[action_result]发现模块PS排行榜完美数分类查看玩家信息流程操作执行成功')
            self.log.info('[action_end]发现模块PS排行榜完美数分类查看玩家信息流程操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]发现模块PS排行榜完美数分类查看玩家信息流程操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('发现模块PS排行榜完美数分类查看玩家信息')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def quitDriver(self):
        self.driver.quitDriver()

if __name__=="__main__":
    faxian=FaXianPageClass()
    faxian.action_add_fjjy()
    faxian.action_psjb_sj()
    faxian.action_psjb_fs()
    faxian.action_psjb_wjs()
    faxian.action_psjb_nd()
    faxian.action_psph_dj()
    faxian.action_psph_jbs()
    faxian.action_psph_yxs()
    faxian.action_psph_wms()