#coding=utf-8
#__author__= 'jws'

import HTMLTestRunner

import os,time
import HTMLTestRunner
import unittest
# from testCase import testCase
from common.send_email import ConfigEmail

def run_case(dir = 'testCase'):
    #按照指定目录加载目标测试用例
    case_dir = os.getcwd() + '\\' + dir
    print(case_dir)
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='testcase*.py',top_level_dir=None)
    return discover

def clear_report():
    nowPath = os.path.dirname(__file__)
    print('nowpath:',nowPath)
    report_path = nowPath + '/' + 'report'
    fileList = os.listdir(report_path)
    if len(fileList)>5:
        for i in fileList:
            file = report_path + '/' + i
            os.remove(file)

    fileNewList = os.listdir(report_path)
    print(fileNewList)

if __name__ == '__main__':
    clear_report()
    current_time = time.strftime("%Y_%m_%d-%H-%M-%S",time.localtime())
    report_path = os.getcwd() + '\\report\\' + current_time + '.html'  #生成测试报告的路径
    print(report_path)
    fp = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'xx公司接口',verbosity=2)
    runner.run(run_case())
    fp.close()
    c = ConfigEmail()
    c.sendEmail()

