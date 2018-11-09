#!/user/bin/env python
#!encoding=utf-8
import time
from Common.LogTools import LogTools
from Common.ReadYamlTools import ReadYamlTools
from Common.ReadXmlTools import ReadXmlTools
from Common.WebdriverTools import WebdriverTools
from Common.PathTools import image_path

'''LoginPage操作函数封装'''

class LoginPageClass:
    def __init__(self):
        '''初始化'''
        self.yamltool=ReadYamlTools('LoginPage.yaml')
        self.xmltool=ReadXmlTools()
        self.log=LogTools()
        self.driver=WebdriverTools()
        self.eleloc=self.yamltool.get_yaml_all_items('LoginPage')
        self.datas=self.xmltool.get_childs_items('LoginPage')

    def action_first_login(self):
        '''登录操作:首次登录'''
        self.log.info('[action_start]首次登录操作执行开始')
        try:
            self.log.info('[action_desc]首次登录')
            self.log.info('[action]进入app介绍页面')
            #app介绍页面
            self.driver.wait_for_element(self.eleloc['element_page1'],10)
            for i in range(2):
                self.driver.swipe_action(630,600,90,600,1000)
                time.sleep(1)
            self.driver.wait_for_element(self.eleloc['element_tips'],3)
            self.driver.element_click(self.eleloc['element_tips'])
            self.driver.wait_for_element(self.eleloc['element_wode'],5)
            self.log.info('[action]点击进入成功')
            #app用户登录
            self.log.info('[action]进入【我的】模块')
            self.driver.element_click(self.eleloc['element_wode'])
            self.driver.wait_for_element(self.eleloc['element_nologin'],5)
            self.driver.element_click(self.eleloc['element_nologin'])
            self.driver.wait_for_element(self.eleloc['element_login_button'],5)
            self.log.info('[action]进入【登录】界面')
            #登录界面输入账号
            self.driver.element_click(self.eleloc['element_username'])
            self.driver.element_clear(self.eleloc['element_username'])
            self.driver.element_sendkeys(self.eleloc['element_username'],self.datas['login_username'])
            #登录界面输入密码
            self.driver.element_click(self.eleloc['element_pwd'])
            self.driver.element_clear(self.eleloc['element_pwd'])
            self.driver.element_sendkeys(self.eleloc['element_pwd'],self.datas['login_pwd'])
            self.driver.element_click(self.eleloc['element_login_button'])
            self.driver.wait_for_element(self.eleloc['element_logout'],15)
            time.sleep(15)
            self.log.info('[action_result]用户登录成功，登录信息如下:')
            self.log.info('[action_result]登录用户名为{}'.format(self.datas['login_username']))
            self.log.info('[action_result]登录密码为{}'.format(self.datas['login_pwd']))
            self.log.info('[action_result]首次登录执行成功')
            self.log.info('[action_end]首次登录操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]首次登录操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('首次登录操作失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_login(self):
        '''登录操作:一般登录'''
        try:
            self.log.info('[action_start]一般登录操作执行开始')
            self.log.info('[action_desc]一般登录')
            self.driver.wait_for_element(self.eleloc['element_wode'],5)
            time.sleep(1)
            self.driver.element_click(self.eleloc['element_wode'])
            # app用户登录
            self.log.info('[action]进入【我的】模块')
            self.driver.wait_for_element(self.eleloc['element_nologin'], 5)
            time.sleep(1)
            self.driver.element_click(self.eleloc['element_nologin'])
            self.driver.wait_for_element(self.eleloc['element_login_button'], 5)
            self.log.info('[action]进入【登录】界面')
            # 登录界面输入账号
            self.driver.element_click(self.eleloc['element_username'])
            self.driver.element_clear(self.eleloc['element_username'])
            self.driver.element_sendkeys(self.eleloc['element_username'], self.datas['login_username'])
            # 登录界面输入密码
            self.driver.element_click(self.eleloc['element_pwd'])
            self.driver.element_clear(self.eleloc['element_pwd'])
            self.driver.element_sendkeys(self.eleloc['element_pwd'], self.datas['login_pwd'])
            self.driver.element_click(self.eleloc['element_login_button'])
            self.driver.wait_for_element(self.eleloc['element_logout'], 15)
            time.sleep(15)
            self.log.info('[action_result]用户登录成功，登录信息如下:')
            self.log.info('[action_result]登录用户名为{}'.format(self.datas['login_username']))
            self.log.info('[action_result]登录密码为{}'.format(self.datas['login_pwd']))
            self.log.info('[action_result]一般登录操作执行成功')
            self.log.info('[action_end]一般登录操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[action_error]一般登录操作执行失败.')
            self.log.error('[action_error]错误原因为{}'.format(e))
            self.driver.get_screenshot_image('一般登录操作失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_logout(self):
        '''注销操作:注销退出'''
        self.log.info('[action_start]注销退出操作执行开始')
        try:
            self.driver.wait_for_element(self.eleloc['element_wode'],10)
            self.driver.element_click(self.eleloc['element_wode'])
            #判断是否已经登录,登录则进行注销退出，未登录则不进行操作
            self.log.info('[action]进入【我的】模块')
            self.driver.wait_for_element(self.eleloc['element_logout'],10)
            self.log.info('[action]账户已经登录，开始注销退出操作')
            self.driver.element_click(self.eleloc['element_logout'])
            self.driver.wait_for_element(self.eleloc['element_logout_tips'],3)
            self.driver.element_click(self.eleloc['element_logout_ok'])
            self.driver.wait_for_element(self.eleloc['element_nologin'],3)
            self.log.info('[action_result]账户注销退出成功')
            self.log.info('[action_end]注销退出操作执行结束')
            self.log.info('---------------------------------------------------------')
        except Exception as e:
            self.log.error('[Error]注销操作执行失败')
            self.log.error('[Error]失败原因为{}'.format(e))
            self.driver.get_screenshot_image('注销退出操作失败')
            self.log.info('[get_image]失败场景已截图，请于{}进行查看'.format(image_path))
            self.log.info('---------------------------------------------------------')
            raise

    def action_goback_shouye(self):
        '''强制回退到主页'''
        self.driver.wait_for_element(self.eleloc['element_tuijian'],100)
        self.driver.element_click(self.eleloc['element_tuijian'])
        self.driver.wait_for_element(self.eleloc['element_tuijian_title'],100)
        time.sleep(5)


    def quitDriver(self):
        self.driver.quitDriver()

if __name__=="__main__":
    loginpage=LoginPageClass()
    loginpage.action_logout()
