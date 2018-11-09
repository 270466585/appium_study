#!/user/bin/env python
#!encoding=utf-8
import os
from Common.PathTools import conf_path
from Common.RewriteConfigParser import RewriteConfigParser

'''读取配置文件封装函数'''

class ReadConfigTools:
    def __init__(self,conf_name='DeviceConfig.ini'):
        '''初始化'''
        #读取配置文件
        self.configfile=os.path.join(conf_path,conf_name)
        self.readconfig=RewriteConfigParser()
        self.readconfig.read(self.configfile)

    def get_conf_all_sections(self):
        '''获取配置文件所有的secitons（列表）'''
        return self.readconfig.sections()

    def get_section_all_options(self,section):
        '''
        获取指定section下的所有options
        :param section: section的值
        :return: 返回所有options(列表)
        '''
        return self.readconfig.options(section)

    def get_section_items(self,section):
        '''
        获取指定section下的items
        :param section: section的值
        :return: 返回items（字典）
        '''
        return dict(self.readconfig.items(section))

    def get_option_value(self,section,option):
        '''
        获取指定section下的指定option的value
        :param section: section值
        :param option: key值
        :return: 返回对应key的value值
        '''
        return self.readconfig.get(section,option)

    def get_conf_all_items(self):
        '''获取配置文件下所有的section下的键值对（字典）'''
        items_dict={}
        all_sections=self.get_conf_all_sections()
        for section in all_sections:
            items=self.get_section_items(section)
            items_dict[section]=items
        return items_dict

    def delete_section_item(self,section,option):
        '''
        删除指定section下的键值对
        :param section: section的值
        :param option: option的值
        :return: 删除指定的键值对
        '''
        self.readconfig.remove_option(section,option)

    def delete_section(self,section):
        '''
        删除指定section
        :param section:section的值
        :return: 删除指定section
        '''
        self.readconfig.remove_section(section)

    def add_conf_section(self,section):
        '''
        添加section
        :param section:section值
        :return: 添加section
        '''
        self.readconfig.add_section(section)

    def add_section_item(self,section,option,value):
        '''
        指定section下添加option:value键值对
        :param section: section值
        :param option: option值
        :param value: value值
        :return: 添加键值对
        '''
        self.readconfig.set(section,option,value)

    def save_conf(self):
        '''修改后保存配置文件内容'''
        with open(self.configfile,'w') as FP:
            self.readconfig.write(FP)


if __name__=="__main__":
    readconfig=ReadConfigTools()
    get_sections=readconfig.get_conf_all_sections()
    get_options=readconfig.get_section_all_options('Device_Configs')
    get_items=readconfig.get_section_items('Device_Configs')
    get_all_items=readconfig.get_conf_all_items()
    print(get_all_items)