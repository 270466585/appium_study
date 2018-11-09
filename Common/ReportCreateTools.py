#!/user/bin/env python
#!encoding=utf-8
import time
import os
import unittest
from Common.PathTools import report_path,testcase_path
from BeautifulReport import BeautifulReport

'''测试报告文件生成相关封装函数'''

class ReportCreateTools:
    def chooseDirCases(self,casedir,pattern):
        '''
        根据指定目录获取匹配的测试用例
        :param casedir: 测试用例目录
        :param pattern: 匹配模式
        :return: 测试用例集
        '''
        casedirpath=os.path.join(testcase_path,'%s/'%casedir)
        discover_cases=unittest.defaultTestLoader.discover(casedirpath,pattern=pattern)
        return discover_cases

    def chooseAllCases(self,pattern):
        '''
        获取TestCases下所有的测试用例
        :param pattern: 匹配模式
        :return: 测试用例集
        '''
        discover_all_cases=unittest.defaultTestLoader.discover(testcase_path,pattern=pattern,top_level_dir=None)
        return discover_all_cases

    def createBeautifulReport(self,title,suite):
        '''
        创建美化的html测试报告
        :param title: 测试报告标题
        :param suite: 用例集
        '''
        try:
            #设定html测试报告文件名称
            nowtime=time.strftime('%Y-%m-%d-%H-%M-%S')
            report_name='BFReport_%s.html'%nowtime
            bf_report_path=os.path.join(report_path,report_name)

            #判断是否存在相同文件，有则先删除
            if os.path.exists(bf_report_path):
                os.remove(bf_report_path)

            #运行测试并生成测试报告
            runcase=BeautifulReport(suite)
            runcase.report(description=title,filename=report_name,log_path=report_path)
        except Exception as e:
            print('[Error] BeautifulReport自动化测试报告生成有误.具体错误为{}'.format(e))
