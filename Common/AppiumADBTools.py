#!/user/bin/env python
#!encoding=utf-8
import re
import os
import time

'''appium_adb相关封装函数'''

class AppiumADBTools:
    def get_all_devicename(self):
        '''自动获取所有设备id信息'''
        #执行cmd
        cmd='adb devices'
        result=list(os.popen(cmd).readlines())
        try:
            #获取设备id
            for i in result:
                if 'device' in i and 'List of devices attached' not in i:
                    pat=re.compile('(.*)\tdevice\n')
                    device_list=re.findall(pat,i)
            return device_list
        except Exception:
            print('[Error]:获取设备连接失败.')
            raise

    def get_one_devicename(self,index):
        '''
        获取指定连接设备的id信息
        :param index:索引
        :return:指定的连接设备信息
        '''
        try:
            devices_list=self.get_all_devicename()
            devicename=devices_list[index]
            if len(devicename)!=0:
                print('[Info]:获取连接设备ID--%s'%devicename)
                return devicename
        except Exception:
            print('[Error]:无设备连接或者连接设备不处于device状态，请检查设备连接.')
            raise

    def check_device(self,index):
        '''
        检查设备是否连接成功
        :param index: 索引
        :return: True/False
        '''
        result=self.get_one_devicename(index)
        if len(result)!=0:
            return True
        else:
            return False

    def get_device_version(self,index):
        '''
        读取指定设备系统版本号
        :param index:索引
        :return:系统版本号
        '''
        devices_version=list(os.popen('adb shell getprop ro.build.version.release').readlines())
        try:
            for i in devices_version:
                pat=re.compile('(.*)\n')
                version_list=re.findall(pat,i)
                print('[Info]:获取设备系统版本号--%s'%version_list[index])
                return version_list[index]
        except Exception:
            print('[Error]:设备系统版本号获取失败.')
            raise

    def get_apk_packageinfo(self,apk_path):
        '''
        获取apk的packageinfo信息
        :param apk_path:apk存放路径
        :return:package信息
        '''
        try:
            package_list=os.popen('aapt dump badging '+apk_path).read()
            pat=re.compile("package: name=\'(.*)\' versionCode")
            package_info=re.search(pat,package_list)
            print('[Info]:获取指定apk的package信息--%s'%package_info.group(1))
            return package_info.group(1)
        except Exception as e:
            print('[Error]:获取apk的package信息失败.')
            print('[Error]:报错具体原因为%s'%e)
            raise


    def get_apk_activity(self,apk_path):
        '''
        获取apk的activity信息
        :param apk_path: apk存放路径
        :return: apk的activity信息
        '''
        try:
            package_list=os.popen('aapt dump badging '+apk_path).read()
            pat=re.compile("launchable-activity: name=\'(.*?)\'")
            activity_info=re.search(pat,package_list)
            print('[Info]:获取指定apk的activity信息--%s'%activity_info.group(1))
            return activity_info.group(1)
        except Exception as e:
            print('[Error]:获取apk的activity信息失败.')
            print('[Error]:报错具体原因为%s' % e)
            raise

    def delete_apkpackage(self,appPackage):
        '''
        删除apk安装包
        :param appPackage: apk安装包信息
        '''
        try:
            cmd='adb uninstall' + appPackage
            os.popen(cmd)
        except Exception as e:
            print('[Error]:获取apk安装包删除失败.')
            print('[Error]:报错具体原因为%s'%e)

    def start_appiumserver(self,port=4723,timeout=60):
        '''
        启动appiumserver
        :param port: 设置端口号，默认为4723
        :param timeout: 设置服务启动超时时间，默认为60s
        '''
        try:
            #启动appium客户端
            cmd='appium -a 127.0.0.1 -p %s'%str(port)
            os.popen(cmd)
            #判断appiumserver是否生成进程号，生成进程号后才算启动成功
            timeout_sec=timeout                     # 设置超时时间
            for sec in range(timeout_sec):
                check_cmd='netstat -o -n -a | findstr %s'%str(port)
                result=os.popen(check_cmd).readlines()
                if len(result)==0:                  # 没有结果则继续等待
                    time.sleep(1)
                    if sec==59 and len(result)==0:
                        print('[Error]:appium服务启动超时，请重新启动.')
                    continue
                else:
                    print('[Info]:appium服务启动成功.')
                    break
        except Exception as e:
            print('[Error]:appium服务启动失败.')
            print('[Error]:具体错误原因:%s'%e)
            raise

    def select_server_pid(self,port=4723):
        '''
        根据端口查询进程号
        :param port:端口号（默认4723）
        :return:获取进程号
        '''
        try:
            cmd='netstat -o -n -a | findstr %s'%str(port)
            get_pid=os.popen(cmd).read()
            pid_str=get_pid.replace(' ','')
            pat=re.compile('TCP127.0.0.1:47230.0.0.0:0LISTENING(.+)')
            pid=re.search(pat,pid_str)
            return pid.group(1)
        except Exception as e:
            print('[Error]:获取appium进程号失败.')
            print('[Error]:具体错误原因:%s' % e)

    def close_appiumserver(self,port=4723):
        '''
        关闭appiumserver
        :param port: 端口号
        '''
        try:
            #杀掉appium服务进程
            pid=self.select_server_pid(port)
            cmd='taskkill /f /pid %s'%str(pid)
            exec_cmd=os.popen(cmd)
            print('[Info]:appium服务关闭成功.')
        except Exception as e:
            print('[Error]:关闭appiumserver失败.')
            print('[Error]:具体错误原因:%s'%e)

if __name__=="__main__":
    abc=AppiumADBTools()
    # devicename=abc.get_one_devicename(0)
    # abc.start_appiumserver()
    # print(abc.get_device_version(0))
    # # print(abc.get_apk_packageinfo(r'D:\PyCharm\Project\APPautotest\appium_autotest_kg\apk\com.p1.mobile.putong_152.apk'))
    # # print(abc.get_apk_activity(r'D:\PyCharm\Project\APPautotest\appium_autotest_kg\apk\com.p1.mobile.putong_152.apk'))
    #
    # abc.close_appiumserver()

