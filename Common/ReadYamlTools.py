#!/user/bin/env python
#!encoding=utf-8
import os
import yaml
from Common.PathTools import elementloc

'''yaml文件获取元素定位信息封装函数'''

class ReadYamlTools:
    def __init__(self,yamlfile):
        '''初始化:读取相应元素定位文件'''
        #指定元素定位文件
        self.yamlfile_path=os.path.join(elementloc,yamlfile)
        try:
            with open(self.yamlfile_path,'r',encoding='utf-8') as eleloc:
                self.eleloc_data=yaml.load(eleloc)
        except Exception as e:
            print('[Error]:未找到指定元素定位文件,具体原因为{}'.format(e))

    def get_yaml_value(self,title,section,option):
        '''
        获取yaml文件中指定section下指定的value
        :param title: yaml的title
        :param section: yaml下的section
        :param option: key值
        :return: 返回指定value值
        '''
        eleloc_title_dict=self.eleloc_data[title]
        eleloc_dict=eleloc_title_dict[section]
        eleloc_value=eleloc_dict[option]
        return eleloc_value

    def get_yaml_all_items(self,title):
        '''
        获取yaml文件中指定title下所有的元素定位
        :param title: yaml的title
        :return: 返回指定title下所有的元素定位（字典）
        '''
        eleloc_dict=self.eleloc_data[title]
        return eleloc_dict

    def get_yaml_section_items(self,title,section):
        '''
        获取yaml文件中指定section下所有的元素定位
        :param title: yaml的title
        :param section: title下指定的section
        :return: 返回指定section下所有元素定位（字典）
        '''
        eleloc_title_dict = self.eleloc_data[title]
        eleloc_dict = eleloc_title_dict[section]
        return eleloc_dict

if __name__=="__main__":
    yamltool=ReadYamlTools('LoginPage.yaml')
    print(yamltool.get_yaml_all_items('LoginPage'))
