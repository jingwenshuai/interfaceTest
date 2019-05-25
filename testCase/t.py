#coding=utf-8
#__author__= 'jws'

import requests

urlstr = 'https://www.wanandroid.com/user/register'
dat = {'username':'liangchao03','password':'123456','repassword':'123456'}
r = requests.post(url=urlstr,data=dat)
print(r.text)
print(r.status_code)