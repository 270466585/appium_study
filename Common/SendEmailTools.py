#!/user/bin/env python
#!encoding=utf-8
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common.PathTools import report_path
from Common.ReadConfigTools import ReadConfigTools

'''邮件发送测试报告相关封装函数'''

class SendEmailTools:
    def __init__(self):
        '''读取配置文件EmailConfig.ini参数'''
        self.readconfig=ReadConfigTools('EmailConfig.ini')
        self.emailconf_itmes=self.readconfig.get_section_items('EMAIL_CONF')

    def get_last_report(self):
        '''获取最新的report文件'''
        try:
            report_list=os.listdir(report_path)
            last_report=report_list[-1]
            last_report_path=os.path.join(report_path,last_report)
            return last_report_path
        except Exception:
            print('[Error]:Report文件夹无测试报告，获取失败.')

    def sendEmail(self,subject,emailfile):
        '''
        发送邮件
        :param subject: 邮件主题
        :param emailfile: 邮件文件
        '''
        # 读取邮件内容
        with open(emailfile,'rb') as fp:
            mail_body=fp.read()

        # 指定发送方与接收方
        sender=self.emailconf_itmes['Email_sender']
        receiver=self.emailconf_itmes['Email_receiver']

        # 配置邮件相关参数
        msg=MIMEText(mail_body,'html','utf-8')
        msg['Subject']=Header(subject,'utf-8')
        msg['From']=sender
        msg['To']=receiver

        # 发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(self.emailconf_itmes['Smtp_connect'])
        smtp.login(self.emailconf_itmes['Smtp_username'], self.emailconf_itmes['Smtp_password'])
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()

    def sendEmailWithFile(self,subject,emailfile):
        '''
        发送邮件（带附件）
        :param subject: 邮件主题
        :param emailfile: 邮件文件
        '''
        # 获取最新文件名称
        report_list=os.listdir(report_path)
        last_report_name=report_list[-1]

        # 读取邮件
        with open(emailfile, 'rb') as fp:
            emailread = fp.read()

        # 指定发送方与接收方
        sender = self.emailconf_itmes['Email_sender']
        receiver = self.emailconf_itmes['Email_receiver']

        # 加载邮件附件
        att = MIMEText(emailread, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment;filename=%s' % last_report_name

        # 配置邮件信息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = Header(subject, "utf-8")
        msgRoot['From'] = sender
        msgRoot['To'] = receiver
        msgRoot.attach(att)

        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.emailconf_itmes['Smtp_connect'])
        smtp.login(self.emailconf_itmes['Smtp_username'], self.emailconf_itmes['Smtp_password'])
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()

if __name__=="__main__":
    email=SendEmailTools()