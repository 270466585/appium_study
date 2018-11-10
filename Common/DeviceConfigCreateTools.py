#!/user/bin/env python
#!encoding=utf-8
import os
from Common.PathTools import conf_path,app_path
from Common.AppiumADBTools import AppiumADBTools

'''DeviceConfig,ini配置文件自动生成封装函数'''

class DeviceConfigCreateTools(AppiumADBTools):
    def create_DeviceConfigs(self,devicesystem='Android',remoteaddr='127.0.0.1',port=4723,
                             noReset=True,unicodeKeyboard=True,
                             resetKeyboard=False,newCommandTimeout=150):
        '''自动生成DeviceConfigs配置文件'''
        configname='DeviceConfig.ini'
        configfile=os.path.join(conf_path,configname)
        #判断配置文件是否存在，存在则删除
        if os.path.exists(configfile):
            os.remove(configfile)
        #指定remoteHost服务端
        remoteHost='http://%s:%s/wd/hub'%(remoteaddr,port)
        #编辑配置文件
        try:
            with open(configfile,'w') as fp:
                fp.write('[Device_Configs]\n')
                fp.write('platformName=%s\n'%devicesystem)
                fp.write('platformVersion=%s\n'%self.get_device_version(0))
                fp.write('deviceName=%s\n'%self.get_one_devicename(0))
                fp.write('appPackage=%s\n'%self.get_apk_packageinfo(app_path))
                fp.write('appActivity=%s\n'%self.get_apk_activity(app_path))
                fp.write('noReset=%s\n'%noReset)
                fp.write('unicodeKeyboard=%s\n'%unicodeKeyboard)
                fp.write('resetKeyboard=%s\n'%resetKeyboard)
                fp.write('newCommandTimeout=%s\n'%str(newCommandTimeout))
                fp.write('remoteHost=%s'%remoteHost)
        except Exception as e:
            print('[Error]:DeviceConfig.ini配置文件生成失败，具体原因为%s'%e)

if __name__=="__main__":
    createconfig=DeviceConfigCreateTools()
    createconfig.create_DeviceConfigs()