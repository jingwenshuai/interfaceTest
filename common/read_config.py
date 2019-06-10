#coding=utf-8
#__author__= 'jws'

import os
import configparser

inifile = os.path.dirname(os.getcwd()) + '\\' + 'config.ini'
# print(inifile)

class ReadConfig(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(inifile,encoding='utf-8')

    #获取配置文件中的分组(EMAIL)中对应的选项的值
    def get_email(self,name):
        value = self.cf.get('EMAIL',name)
        return value

    # def get_http(self,name):
    #     value = self.cf.get('EMAIL',name)


# a = ReadConfig()
# a.get_email('mail_host')