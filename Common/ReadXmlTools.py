#!/user/bin/env python
#!encoding=utf-8
import os
from Common.PathTools import data_path
from xml.etree import ElementTree as ET

'''读取XML文件相关封装函数'''

class ReadXmlTools:
    def __init__(self):
        '''初始化:获取根目录'''
        filename='DataManage.xml'
        self.xmldata_path=os.path.join(data_path,filename)
        self.xmlfile=ET.parse(self.xmldata_path)
        self.root_node=self.xmlfile.getroot()

    def get_node(self,node_path):
        '''
        定位指定节点
        :param node_path: 节点路径
        :return: 指定节点
        '''
        node=self.root_node.find(node_path)
        return node

    def get_node_value(self,node_path):
        '''
        获取指定节点的value
        :param node_path: 节点路径
        :return: 指定节点的value
        '''
        node_text=self.root_node.find(node_path).text
        return node_text

    def get_node_tag(self,node_path):
        '''
        获取指定节点的标签
        :param node_path: 节点路径
        :return: 指定节点的标签
        '''
        node_tag=self.root_node.find(node_path).tag
        return node_tag

    def get_node_attribute(self,node_path,attribute):
        '''
        获取指定节点的属性
        :param node_path: 节点路径
        :param attribute: 属性
        :return: 指定节点的属性对应值
        '''
        node=self.root_node.find(node_path)
        node_attribute=node.get(attribute)
        return node_attribute

    def get_node_childs(self,node_path=None):
        '''
        获取指定父类下的所有子节点
        :param node_path: 指定父类节点，默认为None则为根目录
        :return: 返回子节点列表
        '''
        child_nodes_list=[]
        #node_path为None则获取根目录所有子节点
        if node_path==None:
            for child_node in self.root_node:
                child_nodes_list.append(child_node)
        #node_path不为None则获取指定目录所有子节点
        else:
            father_node=self.get_node(node_path)
            for child_node in father_node:
                child_nodes_list.append(child_node)
        return child_nodes_list

    def get_childs_items(self,node_path):
        '''
        获取父节点下所有子节点的键值对，{tag:value}
        :param node_path: 父节点路径
        :return: {tag:value}字典
        '''
        child_items={}
        try:
            father_node=self.get_node(node_path)
            for child_node in father_node:
                child_items[child_node.tag]=child_node.text
            return child_items
        except Exception:
            print('[Error]:获取子节点键值对失败.')


if __name__=="__main__":
    xmltool=ReadXmlTools()
    print(xmltool.get_node('Common/browser'))
    print(xmltool.get_node_childs())
    print(xmltool.get_childs_items('Common/email'))
