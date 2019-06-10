#coding=utf-8
#__author__= 'jws'

import requests

class ReadHttp:

    #定义get方法
    def get(self,url,param,data=None,cookie=None,header=None):
        try:
            print(url,param)
            response = requests.get(url=url,params=param)
            result = response.text
            return result
        except Exception as msg:
            print('please check out!-->',msg)
            return None

    #定义post方法
    def post(self,url,param):
        try:
            print(url,param)
            response = requests.post(url=url,data=param)
            result = response.text
            return result
        except Exception as msg:
            print('please check out!-->',msg)
            return None

    #定义put方法
    def put(self,url,param):
        try:
            print(url,param)
            response = requests.put(url=url)
            result = response.text
            return result
        except Exception as msg:
            print('please check out!-->',msg)
            return None

    #定义通过传参判断需要调用的方法
    def get_Request(self,url,method,param):
        if str(method) == 'get':
            return self.get(url,param)
        elif str(method) == 'post':
            return self.post(url,param)
        elif str(method) == 'put':
            return self.put(url,param)