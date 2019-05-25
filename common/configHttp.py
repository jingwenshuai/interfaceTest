#coding=utf-8
#__author__= 'jws'

import requests

class ConfigHttp(object):

    def get(self,url,param):
        try:
            print(url,param)
            response = requests.get(url,params=eval(param))
            result = response.text
            #获取实际结果，进行断言
            return result
        except Exception:
            print('request errot,please check out!')
            return None

    def post(self,url,param):

