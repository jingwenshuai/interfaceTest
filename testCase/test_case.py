#coding=utf-8
#__author__= 'jws'

import unittest,json
from ddt import ddt,data,unpack
#调用readExcel模块拿到测试数据
from common import readExcel
from common.writeExcel import writeExcel
from common.configHttp import ConfigHttp


#获取读到的数据
testdata = readExcel.readExcel().addDate()
print(testdata)
@ddt
class MyTestCase1(unittest.TestCase):

    @data(*testdata)
    @unpack
    def test_normal(self,id,url,method,param,expect):
        result = re.getRequest(url,method,param)
        real = str(json.loads(result)['errorCode'])
        try:
            status = self.assertEqual(real,expect)
            print('返回结果：'status)
        except AssertionError as msg:
            print(msg)
            status = 'Error'
        finally:
            if status == 'None':
                wr.writeData(id,real,'Success')
            else:
                wr.writeData(id,real,'Failed')

if __name__ == '__main__':
    unittest.main()