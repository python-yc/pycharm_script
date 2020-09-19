# -*- coding: utf-8 -*-

import requests

"""
requests的get或者post请求，返回的响应response获取方法：content和text
content用于获取图片，返回二进制数据
text用于获取内容，返回的是unicode解码字符串
"""
url = "http://www.baidu.com"
# 两种请求方式
rsp = requests.get(url)

print(rsp.text)

print("==================================")

rsp = requests.request("get", url)

print(rsp.content)



