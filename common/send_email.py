#coding=utf-8
#__author__= 'jws'

import smtplib,os
from common.read_config import ReadConfig
from email.mime.text import MIMEText
from email.header import Header

class ConfigEmail():
    #实例化导入的ReadConfig类
    rc = ReadConfig()

    #读取ini配置文件中邮箱属性
    mail_host = rc.get_email('mail_host')
    mail_user = rc.get_email('mail_user')
    mail_pass = rc.get_email('mail_pass')

    sender = rc.get_email('sender')
    receiver = rc.get_email('receiver')
    content = rc.get_email('content')
    testuser = rc.get_email('testuser')

    #配置发送内容   # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText('wew', _subtype='plain', _charset='utf-8')    #邮件内容
    msg['Subject'] = Header(content, 'utf-8')                           #邮件标题
    msg['From'] = sender
    msg['To'] = receiver


    #创建发送邮件方法
    def sendEmail(self):
        try:
            #实例化邮箱
            smtp = smtplib.SMTP()
            #连接smtp服务器
            smtp.connect(self.mail_host)
            #登陆邮箱
            smtp.login(user=self.mail_user,password=self.mail_pass)
            smtp.sendmail(self.sender,self.receiver,self.msg.as_string())
        except:
            print('Fail')
        else:
            print('success')
        finally:
            smtp.quit()


# a = ConfigEmail()
# a.sendEmail()