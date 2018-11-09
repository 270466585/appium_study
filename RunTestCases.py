#!/user/bin/env python
#!encoding=utf-8
from Common.ReportCreateTools import ReportCreateTools
from Common.SendEmailTools import SendEmailTools
'''执行自动化用例并生成测试报告、发送测试报告邮件'''

#执行用例并生成报告
runtool=ReportCreateTools()
suite=runtool.chooseAllCases('test*')
runtool.createBeautifulReport('A9VG自动化测试报告',suite)

#发送测试报告邮件
emailtool=SendEmailTools()
lastfile=emailtool.get_last_report()
emailtool.sendEmailWithFile('A9VG自动化测试报告',lastfile)