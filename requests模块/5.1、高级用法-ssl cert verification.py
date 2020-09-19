# -*- coding: utf-8 -*-
# 证书验证(大部分网站都是https)
import requests

'''如果是ssl请求,首先检查证书是否合法,不合法则报错,程序终端'''
# 这里不报错，不知道为什么
rsp1 = requests.get('https://www.12306.cn')

'''改进1:去掉报错,但是会报警告'''
print('改进1:去掉报错,但是会报警告')
# 不验证证书,报警告,返回200
# rsp2 = requests.get('https://www.12306.cn', verify=False)
# print(rsp2.status_code)

'''改进2：去掉报错，并去掉告警信息'''
print('改进2：去掉报错，并去掉告警信息')
from requests.packages import urllib3

urllib3.disable_warnings()  # 关闭警告
rsp3 = requests.get('https://www.12306.cn', verify=False)

print(rsp3.status_code)

'''改进3：加上证书
很多网站都是https，但是不用证书也可以访问，大多数情况都是可以携带也可以不携带证书
知乎、百度等都是可带可不带
有硬性要求的必须携带，比如对应定向的用户，拿到证书后才有权限访问某个网站

当然要真的有
'''
print('改进3：加上证书')

# rsp4 = requests.get('https://www.12306.cn',
#                     cert=('/path/server.crt', '/path/key')
#                     )

# print(rsp4.status_code)
