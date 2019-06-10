#coding=utf-8
#__author__= 'jws'

import os,time
import unittest
from myfun import *
import HTMLTestRunner

class myTest(unittest.TestCase):

    def setUp(self):
        print('up')

    def tearDown(self):
        print('dowm')

    def test_a(self):
        self.assertEqual(add(1,2),3)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    current_time = time.strftime("%Y_%m_%d-%H-%M-%S",time.localtime())
    report_path = os.getcwd() + '\\report' + current_time + '.html'
    fp = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'xx公司接口',verbosity=2)
    runner.run(suite)
    fp.close()
