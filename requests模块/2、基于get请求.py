# -*- coding: utf-8 -*-
"""
代码分析Python requests库 中文编码问题
http://xiaorui.cc/archives/2786
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
}

"""1、基本请求"""
response = requests.get('http://dig.chouti.com/')
# print(response.text)

"""2.1、带参数的get请求 -> params"""

url = 'https://www.baidu.com/s?wd=python&pn=1'

rsp = requests.get(url, headers=headers)

# 直接输出是有乱码的，因此需要对编码格式处理
# print(rsp.text)

print(rsp.encoding)  # ISO-8859-1
print(type(rsp.text))  # <class 'str'>
print(type(rsp.content))  # <class 'bytes'>
print(rsp.apparent_encoding)  # utf-8
# rsp.encoding = rsp.apparent_encoding

"""2.2、如果关键词是中文或者有其它特殊符号，则需要进行url编码"""
from urllib.parse import urlencode

wd = '你好'
keyword = urlencode({'k': wd}, encoding='utf-8').split('=')[-1]
url = 'https://www.baidu.com/s?wd=%s&pn=1' % keyword
rsp = requests.get(url, headers=headers)

"""3、带参数的get请求 -> headers"""
# 通常我们在发送请求时都需要带上请求头，请求头是将自身伪装成浏览器的关键，常见的有用的请求头如下
# Host
# Referer #大型网站通常都会根据该参数判断请求的来源
# User-Agent #客户端
# Cookie #Cookie信息虽然包含在请求头里，但requests模块有单独的参数来处理他，headers={}内就不要放它了

# 添加headers(浏览器会识别请求头,不加可能会被拒绝访问,比如访问https://www.zhihu.com/explore)
response = requests.get('https://www.zhihu.com/explore')
print(response.status_code) # 500

rsp = requests.get('https://www.zhihu.com/explore', headers=headers)
print(rsp.status_code)  # 200

"""带参数的get请求cookies"""
cookies = {
    'user_session': 'rzNme4L6LTH7QSresq8wo0BVYhTNt5GS-asNnkOe7_FZ2CjB6',
}

# github对请求对没什么限制，我们无需定制user-agent，其它网站还是需要的
rsp = requests.get('https://github.com/settings/emails',
                   cookies=cookies)

print('306334678@qq.com' in response.text)  # True
