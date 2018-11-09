#!/user/bin/env python
#!encoding=utf-8
import time
from Common.ReadYamlTools import ReadYamlTools
from Common.ReadXmlTools import ReadXmlTools
from Common.WebdriverTools import WebdriverTools

'''封装登录动作，用于后续自动化跑流程'''

class LoginAction:
    def __init__(self):
        '''初始化'''
        self.yamltool=ReadYamlTools('LoginPage.yaml')
        self.xmltool=ReadXmlTools()
        self.driver=WebdriverTools()
        self.ele_loc=self.yamltool.get_yaml_all_items('LoginPage')
        self.datas=self.xmltool.get_childs_items('LoginPage')

    def action_checklogin(self):
        '''判断登录app时用户是否登录:
           第一种情况:检查【我的】界面，若已经登录，则返回到首页
           第二种情况:检查【我的】界面，若没有登录，则直接进行登录，登录后返回首页
        '''
        self.driver.wait_for_element(self.ele_loc['element_wode'],10)
        self.driver.element_click(self.ele_loc['element_wode'])
        time.sleep(5)
        #用户没有登录则进行登录操作
        try:
            self.driver.wait_for_element(self.ele_loc['element_nologin'],10)
            self.driver.element_click(self.ele_loc['element_nologin'])
            self.driver.wait_for_element(self.ele_loc['element_login_button'],10)
            #输入账号
            self.driver.element_click(self.ele_loc['element_username'])
            self.driver.element_clear(self.ele_loc['element_username'])
            self.driver.element_sendkeys(self.ele_loc['element_username'],self.datas['login_username'])
            #输入密码
            self.driver.element_click(self.ele_loc['element_pwd'])
            self.driver.element_sendkeys(self.ele_loc['element_pwd'],self.datas['login_pwd'])
            #点击登录按钮
            self.driver.element_click(self.ele_loc['element_login_button'])
            #验证是否登录成功
            self.driver.wait_for_element(self.ele_loc['element_logout'],10)
            print('[action_result]用户登录成功')
        #用户已经登录则返回推荐页面
        except:
            self.driver.wait_for_element(self.ele_loc['element_logout'],10)
            self.driver.element_click(self.ele_loc['element_tuijian'])
            self.driver.wait_for_element(self.ele_loc['element_tuijian_title'],10)
            print('[action_result]用户已经登录，无需登录，已跳转推荐页面')


if __name__=="__main__":
    loginaction=LoginAction()
    loginaction.action_checklogin()