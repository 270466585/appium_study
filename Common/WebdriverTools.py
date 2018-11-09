#!/user/bin/env python
#!encoding=utf-8
import os
import time
from appium import webdriver
from Common.ReadConfigTools import ReadConfigTools
from Common.PathTools import app_path,image_path

'''appium的webdriver相关封装函数'''

class WebdriverTools:
    def __init__(self):
        '''初始化:获取配置文件并指定app包'''
        self.readconf=ReadConfigTools()
        self.desired_caps=self.readconf.get_section_items('Device_Configs')
        self.desired_caps['app']=app_path
        self._driver = webdriver.Remote(self.desired_caps['remoteHost'], self.desired_caps)

    def quitDriver(self):
        '''关闭webdriver'''
        if self._driver:
            self._driver.quit()

    '''================================元素定位================================'''

    def find_element(self,eleinfo):
        '''
        元素定位（单个元素）
        :param eleinfo:元素定位信息
        :return:定位元素
        '''
        # xpath定位
        if eleinfo.startswith("//"):
            element=self._driver.find_element_by_xpath(eleinfo)
        #id定位
        elif ":id/" in eleinfo or ":string/" in eleinfo:
            element=self._driver.find_element_by_id(eleinfo)
        else:
            #name定位
            try:
                element=self._driver.find_element_by_name(eleinfo)
            #class_name定位
            except:
                element=self._driver.find_element_by_class_name(eleinfo)
        return element

    def find_elements(self,eleinfo):
        '''
        元素集定位（多个元素）
        :param eleinfo:元素定位信息
        :return:定位元素集
        '''
        # xpath定位
        if eleinfo.startswith("//"):
            elements=self._driver.find_elements_by_xpath(eleinfo)
        #id定位
        elif ":id/" in eleinfo or ":string/" in eleinfo:
            elements=self._driver.find_elements_by_id(eleinfo)
        else:
            #name定位
            try:
                elements=self._driver.find_elements_by_name(eleinfo)
            #class_name定位
            except:
                elements=self._driver.find_elements_by_class_name(eleinfo)
        return elements


    def get_ele_from_elements(self,eleinfo,index):
        '''
        元素集定位，获取其中某一个定位元素
        :param eleinfo: 元素定位信息
        :param index: 索引
        :return: 返回元素集某一个定位元素
        '''
        elementslist=self.find_elements(eleinfo)
        element=elementslist[index]
        return element

    def check_element_isshown(self,eleinfo):
        '''
        判断定位元素是否显示在页面
        :param eleinfo: 元素定位信息
        :return: True/False
        '''
        if self.find_element(eleinfo):
            return True
        else:
            return False

    def check_one_of_eles_isshown(self,eleinfo,index):
        '''
        判断元素集指定元素是否显示在页面
        :param eleinfo: 元素集定位信息
        :param index: 索引
        :return: True/False
        '''
        try:
            if self.get_ele_from_elements(eleinfo,index):
                return True
        except:
            return False

    def wait_for_element(self,eleinfo,period):
        '''
        等待元素出现
        :param eleinfo: 元素定位信息
        :param period: 等待时间
        '''
        try:
            for i in range(period):
                time.sleep(1)
                if self.check_element_isshown(eleinfo)==True:
                    break
        except Exception:
            print('[Warning]:定位元素{}失败.再次进行等待元素'.format(eleinfo))

    def wait_for_one_of_eles(self,eleinfo,index,period):
        '''
        等待元素集指定元素出现
        :param eleinfo: 元素集定位信息
        :param index: 索引
        :param period: 等待时间
        '''
        try:
            for i in range(period):
                time.sleep(1)
                if self.check_one_of_eles_isshown(eleinfo,index)==True:
                    break
        except Exception:
            print('[Warning]:定位元素{}失败.再次进行等待元素'.format(eleinfo))

    '''================================元素操作================================'''

    def element_click(self,eleinfo):
        '''
        元素操作:click点击
        :param eleinfo:单个元素定位信息
        '''
        element=self.find_element(eleinfo)
        element.click()

    def element_clear(self,eleinfo):
        '''
        元素操作:清空
        :param eleinfo:单个元素定位信息
        '''
        element=self.find_element(eleinfo)
        element.clear()

    def element_sendkeys(self,eleinfo,msg):
        '''
        元素操作:输入内容
        :param eleinfo:单个元素定位信息
        :param msg: 输入内容
        '''
        element=self.find_element(eleinfo)
        element.send_keys(msg)

    def element_tap(self,start_x,start_y,end_x,end_y,msec):
        '''
        元素操作:tap点击
        :param start_x: x轴元素起始坐标
        :param start_y: y轴元素起始坐标
        :param end_x: x轴元素终点坐标
        :param end_y: y轴元素终点坐标
        :param msec: 点击评率（毫秒）
        '''
        start_xy=[start_x,start_y]
        end_xy=[end_x,end_y]
        self._driver.tap(start_xy,end_xy,msec)

    def one_of_elements_click(self,eleinfo,index):
        '''
        元素集操作:点击
        :param eleinfo:元素集定位信息
        :param index: 索引
        '''
        element=self.get_ele_from_elements(eleinfo,index)
        element.click()

    def one_of_elements_clear(self,eleinfo,index):
        '''
        元素集操作:清空
        :param eleinfo:元素集定位信息
        :param index: 索引
        '''
        element=self.get_ele_from_elements(eleinfo,index)
        element.clear()

    def one_of_elements_sendkeys(self,eleinfo,index,msg):
        '''
        元素集操作:输入内容
        :param eleinfo: 元素集定位信息
        :param index: 索引
        '''
        element=self.get_ele_from_elements(eleinfo,index)
        element.send_keys(msg)

    def swipe_action(self,start_x,start_y,end_x,end_y,msec):
        '''
        滑动操作
        :param start_x: x轴开始位置
        :param start_y: y轴开始位置
        :param end_x: x轴结束位置
        :param end_y: y轴结束位置
        :param msec: 滑动时间（毫秒）
        '''
        self._driver.swipe(start_x,start_y,end_x,end_y,msec)

    def get_element_size(self,eleinfo):
        '''
        获取指定元素的size
        :param eleinfo: 单个元素定位信息
        :return: 返回宽和高
        '''
        element_size=self.find_element(eleinfo).size
        element_width=element_size.get('width')
        element_height=element_size.get('height')
        return element_width,element_height

    def get_one_of_elements_size(self,eleinfo,index):
        '''
        获取元素集指定元素的size
        :param eleinfo: 元素集定位信息
        :param index: 索引
        :return: 返回宽和高
        '''
        element_size=self.get_ele_from_elements(eleinfo,index)
        element_width=element_size.get('width')
        element_height=element_size.get('height')
        return element_width,element_height

    def get_element_location(self,eleinfo):
        '''
        获取指定元素的坐标
        :param eleinfo:指定元素定位信息
        :return: x轴坐标与y轴坐标
        '''
        element_loc=self.find_element(eleinfo).location
        element_x=element_loc.get('x')
        element_y=element_loc.get('y')
        return element_x,element_y

    def get_one_of_elements_location(self,eleinfo,index):
        '''
        获取元素集指定元素的坐标
        :param eleinfo:元素集定位信息
        :param index:索引
        :return: x轴坐标和y轴坐标
        '''
        element_loc=self.get_ele_from_elements(eleinfo,index)
        element_x=element_loc.get('x')
        element_y=element_loc.get('y')
        return element_x,element_y

    def ele_zwy_swipe(self,eleinfo,msec):
        '''
        定位元素左往右滑动
        :param eleinfo:指定元素定位信息
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_element_size(eleinfo)
        element_x,element_y=self.get_element_location(eleinfo)
        start_x=element_x+50                                    #开始滑动x轴坐标
        start_y=element_y-element_height+element_height/2       #计算元素y轴中间点
        end_x=element_width-50                                  #结束滑动x轴坐标
        end_y=start_y                                           #y轴中间点
        self.swipe_action(start_x,start_y,end_x,end_y,msec)

    def one_of_eles_zwy_swipe(self,eleinfo,index,msec):
        '''
        元素集定位元素左往右滑动
        :param eleinfo: 元素集定位信息
        :param index: 索引
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_one_of_elements_size(eleinfo,index)
        element_x,element_y=self.get_one_of_elements_location(eleinfo,index)
        start_x=element_x+50                                    #开始滑动x轴坐标
        start_y=element_y-element_height+element_height/2       #计算元素y轴中间点
        end_x=element_width-50                                  #结束滑动x轴坐标
        end_y=start_y                                           #y轴中间点
        self.swipe_action(start_x,start_y,end_x,end_y,msec)

    def ele_ywz_swipe(self,eleinfo,msec):
        '''
        指定元素右往左滑动
        :param eleinfo:指定元素定位信息
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_element_size(eleinfo)
        element_x,element_y=self.get_element_location(eleinfo)
        start_x=element_width-50
        start_y=element_y-element_height+element_height/2
        end_x=element_x+50
        end_y=start_y
        self.swipe_action(start_x,start_y,end_x,end_y,msec)

    def one_of_eles_ywz_swipe(self,eleinfo,index,msec):
        '''
        元素集指定元素右往左滑动
        :param eleinfo: 元素集定位元素信息
        :param index: 索引
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_one_of_elements_size(eleinfo,index)
        element_x,element_y=self.get_one_of_elements_location(eleinfo,index)
        start_x = element_width - 50
        start_y = element_y - element_height + element_height / 2
        end_x = element_x + 50
        end_y = start_y
        self.swipe_action(start_x, start_y, end_x, end_y, msec)

    def ele_swx_swipe(self,eleinfo,msec):
        '''
        指定元素上往下滑动
        :param eleinfo: 元素定位信息
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_element_size(eleinfo)
        element_x,element_y=self.get_element_location(eleinfo)
        start_x=element_x-element_width+element_width/2         #计算x轴中间点
        start_y=element_y-element_height+50                     #上面y轴起点
        end_x=start_x                                           #x轴中间点
        end_y=element_y-50                                      #下面y轴终点
        self.swipe_action(start_x, start_y, end_x, end_y, msec)

    def one_of_eles_swx_swipe(self,eleinfo,index,msec):
        '''
        元素集指定元素上往下滑动
        :param eleinfo: 元素集定位信息
        :param index: 索引
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_one_of_elements_size(eleinfo,index)
        element_x,element_y=self.get_one_of_elements_location(eleinfo,index)
        start_x = element_x - element_width + element_width / 2  # 计算x轴中间点
        start_y = element_y - element_height + 50                # 上面y轴起点
        end_x = start_x                                          # x轴中间点
        end_y = element_y - 50                                   # 下面y轴终点
        self.swipe_action(start_x, start_y, end_x, end_y, msec)

    def ele_xws_swipe(self,eleinfo,msec):
        '''
        指定元素下往上滑动
        :param eleinfo:元素定位信息
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_element_size(eleinfo)
        element_x,element_y=self.get_element_location(eleinfo)
        start_x=element_x-element_width+element_width/2
        start_y=element_y-50
        end_x=start_x
        end_y=element_y-element_height+50
        self.swipe_action(start_x, start_y, end_x, end_y, msec)

    def one_of_eles_xws_swipe(self,eleinfo,index,msec):
        '''
        元素集指定元素下往上滑动
        :param eleinfo: 元素集定位信息
        :param index: 索引
        :param msec: 滑动时间（毫秒）
        '''
        element_width,element_height=self.get_one_of_elements_size(eleinfo,index)
        element_x,element_y=self.get_one_of_elements_location(eleinfo,index)
        start_x = element_x - element_width + element_width / 2
        start_y = element_y - 50
        end_x = start_x
        end_y = element_y - element_height + 50
        self.swipe_action(start_x, start_y, end_x, end_y, msec)

    def get_ele_center(self,eleinfo):
        '''
        获取指定元素的中点坐标
        :param eleinfo: 指定元素定位信息
        :return: 中点x与y轴坐标
        '''
        element_width,element_height=self.get_element_size(eleinfo)
        element_x,element_y=self.get_element_location(eleinfo)
        center_x=element_x-element_width+element_width/2
        center_y=element_y-element_height+element_height/2
        return center_x,center_y

    def get_one_of_eles_center(self,eleinfo,index):
        '''
        获取元素集指定元素的中点坐标
        :param eleinfo: 指定元素定位信息
        :param index: 索引
        :return: 中点x与y轴坐标
        '''
        element_width,element_height=self.get_one_of_elements_size(eleinfo,index)
        element_x,element_y=self.get_one_of_elements_location(eleinfo,index)
        center_x = element_x - element_width + element_width / 2
        center_y = element_y - element_height + element_height / 2
        return center_x, center_y

    '''================================模拟按键操作================================'''
    def press_Homebutton(self):
        '''按下Home键'''
        self._driver.long_press_keycode('3')

    def press_Backbutton(self):
        '''按下返回键'''
        self._driver.long_press_keycode(4)

    def press_Searchbutton(self):
        '''按下搜索键'''
        self._driver.long_press_keycode('84')

    def press_Enterbutton(self):
        '''按下回车键'''
        self._driver.long_press_keycode('66')

    def press_Delbutton(self):
        '''按下退格键'''
        self._driver.long_press_keycode('67')

    '''================================数字/字母按键操作================================'''
    #数字按键
    def press_num_0(self):
        '''数字键0'''
        self._driver.long_press_keycode('7')

    def press_num_1(self):
        '''数字键1'''
        self._driver.long_press_keycode('8')

    def press_num_2(self):
        '''数字键2'''
        self._driver.long_press_keycode('9')

    def press_num_3(self):
        '''数字键3'''
        self._driver.long_press_keycode('10')

    def press_num_4(self):
        '''数字键4'''
        self._driver.long_press_keycode('11')

    def press_num_5(self):
        '''数字键5'''
        self._driver.long_press_keycode('12')

    def press_num_6(self):
        '''数字键6'''
        self._driver.long_press_keycode('13')

    def press_num_7(self):
        '''数字键7'''
        self._driver.long_press_keycode('14')

    def press_num_8(self):
        '''数字键8'''
        self._driver.long_press_keycode('15')

    def press_num_9(self):
        '''数字键9'''
        self._driver.long_press_keycode('16')

    #字母按键
    def press_code_A(self):
        '''字母键A'''
        self._driver.long_press_keycode('29')

    def press_code_B(self):
        '''字母键B'''
        self._driver.long_press_keycode('30')

    def press_code_C(self):
        '''字母键C'''
        self._driver.long_press_keycode('31')

    def press_code_D(self):
        '''字母键D'''
        self._driver.long_press_keycode('32')

    def press_code_E(self):
        '''字母键E'''
        self._driver.long_press_keycode('33')

    def press_code_F(self):
        '''字母键F'''
        self._driver.long_press_keycode('34')

    def press_code_G(self):
        '''字母键G'''
        self._driver.long_press_keycode('35')

    def press_code_H(self):
        '''字母键H'''
        self._driver.long_press_keycode('36')

    def press_code_I(self):
        '''字母键I'''
        self._driver.long_press_keycode('37')

    def press_code_J(self):
        '''字母键J'''
        self._driver.long_press_keycode('38')

    def press_code_K(self):
        '''字母键K'''
        self._driver.long_press_keycode('39')

    def press_code_L(self):
        '''字母键L'''
        self._driver.long_press_keycode('40')

    def press_code_M(self):
        '''字母键M'''
        self._driver.long_press_keycode('41')

    def press_code_N(self):
        '''字母键N'''
        self._driver.long_press_keycode('42')

    def press_code_O(self):
        '''字母键O'''
        self._driver.long_press_keycode('43')

    def press_code_P(self):
        '''字母键P'''
        self._driver.long_press_keycode('44')

    def press_code_Q(self):
        '''字母键Q'''
        self._driver.long_press_keycode('45')

    def press_code_R(self):
        '''字母键R'''
        self._driver.long_press_keycode('46')

    def press_code_S(self):
        '''字母键S'''
        self._driver.long_press_keycode('47')

    def press_code_T(self):
        '''字母键T'''
        self._driver.long_press_keycode('48')

    def press_code_U(self):
        '''字母键U'''
        self._driver.long_press_keycode('49')

    def press_code_V(self):
        '''字母键V'''
        self._driver.long_press_keycode('50')

    def press_code_W(self):
        '''字母键W'''
        self._driver.long_press_keycode('51')

    def press_code_X(self):
        '''字母键X'''
        self._driver.long_press_keycode('52')

    def press_code_Y(self):
        '''字母键Y'''
        self._driver.long_press_keycode('53')

    def press_code_Z(self):
        '''字母键Z'''
        self._driver.long_press_keycode('54')

    '''================================截图操作================================'''
    def nowtime(self):
        '''获取当前时间'''
        nowtime=time.strftime('%Y%m%d_%H%M%S')
        return nowtime

    def curdate(self):
        '''获取当前日期'''
        curdate=time.strftime('%Y%m%d')
        return curdate

    def get_screenshot_image(self,imagename):
        '''
        截图操作
        :param imagename: 截图名称
        '''
        gettime=self.nowtime()
        curdate=self.curdate()
        image_dir_path=os.path.join(image_path,curdate)
        if os.path.exists(image_dir_path)!=True:      #自动创建日期文件夹
            os.mkdir(image_dir_path)
        imagefile_path=os.path.join(image_dir_path,'%s_%s.png'%(imagename,gettime))
        self._driver.get_screenshot_as_file(imagefile_path)

