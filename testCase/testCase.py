#coding=utf-8
#__author__= 'jws'
'''
功能：
    1，获取读取excel并重构后返回的数据
    2，请求requests方法
    3，断言
    4，写入excel
'''

import unittest,json
from ddt import ddt,data,unpack
from common.read_excel_test import ReadExcel
from common.read_Http_test import ReadHttp
from common.write_Excel_test import WriteExcel

#实例化类
readEx = ReadExcel()
testdata = readEx.addData()
print(testdata)
readHt = ReadHttp()
writeEx = WriteExcel()

@ddt
class MyTestCase(unittest.TestCase):

    @data(*testdata)
    @unpack
    def test_normal(self,id,url,method,param,expect):
        print(id,url,method,param,expect)
        print(type(eval(param)))
        result = readHt.get_Request(url,method,param)
        real = str(json.loads(result)['errorCode'])
        try:
            status = self.assertEqual(real,expect)
            print('返回结果：',status)
        except AssertionError as msg:
            print(msg)
            status = 'Error'
        finally:
            if status ==None:
                writeEx.writeData(id,real,'Success')
            else:
                writeEx.writeData(id,real,'Fail')

if __name__ == '__main__':
    unittest.main()






