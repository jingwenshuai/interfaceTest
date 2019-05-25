#coding=utf-8
#__author__= 'jws'

import re
import requests,json

#调用readExcel模块拿到测试数据
from common import readExcel
#

#根据接口的请求方式判断调用什么方法(get/post)

res = readExcel.readExcel().addDate()

for i in res:
    # print(i)
    urlstr = i[1]
    # print('i5:',i[5])
    # print('tyi5:',type(i[5]))
    errorcod = int(i[5])
    # print(errorcod)
    # print(type(errorcod))
    if i[3] == 'get':
        parm = eval(i[4])
        # print(urlstr,parm)
        r = requests.get(url=urlstr,params=parm)
        # print(r.status_code)
    elif i[3] == 'post':
        dat = eval(i[4])
        # print(type(dat))
        # print('###dat:',dat)
        r = requests.post(url=urlstr,data=dat)
        # print('post')
        # print(r.status_code)
        print(r.text)
    #校验
    # print('json:',r.json()['errorCode'])
    # print(type(r.json()['errorCode']))
    if r.status_code == 200 and r.json()['errorCode']==errorcod:
        print('请求成功')
    else:
        print('请求失败')






# urlstr = 'https://wanandroid.com/user/login'
# param = {'username':'jingwenshuai','password':'123456'}
# r = requests.post(url=urlstr,data=param)
# print(r.status_code)
# a = r.text
# print(a)
# res = re.search('^jingwenshuai',a)
# print(res)

#get/post请求

#校验

#保存执行结果

#写入excel中

