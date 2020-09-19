# -*- coding: utf-8 -*-
## 3.1 介绍
"""
#GET请求
HTTP默认的请求方法就是GET
     * 没有请求体
     * 数据必须在1K之内！
     * GET请求数据会暴露在浏览器的地址栏中

GET请求常用的操作：
       1. 在浏览器的地址栏中直接给出URL，那么就一定是GET请求
       2. 点击页面上的超链接也一定是GET请求
       3. 提交表单时，表单默认使用GET请求，但可以设置为POST


#POST请求
(1). 数据不会出现在地址栏中
(2). 数据的大小没有上限
(3). 有请求体
(4). 请求体中如果存在中文，会使用URL编码！


#！！！requests.post()用法与requests.get()完全一致，特殊的是requests.post()有一个data参数，用来存放请求体数据
"""
## 3.2、发送post请求，墨迹浏览器的登录行为

import requests
import re

'''
### 对于登录来说，应该输错用户名或密码然后分析抓包流程，用脑子想一想，输对了浏览器就跳转了，还分析个毛线，累死你也找不到包

一 目标站点分析
    浏览器输入https://github.com/login
    然后输入错误的账号密码，抓包
    发现登录行为是post提交到：https://github.com/session
    而且请求头包含cookie
    而且请求体包含：
        commit:Sign in
        utf8:✓
        authenticity_token:lbI8IJCwGslZS8qJPnof5e7ZkCoSoMn6jmDTsL1r/m06NLyIbw7vCrpwrFAPzHMep3Tmf/TSJVoXWrvDZaVwxQ==
        login:egonlin
        password:123
二 流程分析
    先GET：https://github.com/login拿到初始cookie与authenticity_token
    返回POST：https://github.com/session， 带上初始cookie，带上请求体（authenticity_token，用户名，密码等）
    最后拿到登录cookie

    ps：如果密码时密文形式，则可以先输错账号，输对密码，然后到浏览器中拿到加密后的密码，github的密码是明文
'''
r1 = requests.get('https://github.com/login')
r1_cookie = r1.cookies.get_dict()  # 拿到初始cookie(未被授权)

authenticity_token = \
    re.findall(r'name="authenticity_token".*?value="(.*?)"', r1.text)[
        0]  # 从页面中拿到CSRF TOKEN

# 第二次请求：带着初始cookie和TOKEN发送POST请求给登录页面，带上账号密码
data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': 'python-yc',
    'password': 'yc13705676620'
}

r2 = requests.post('https://github.com/session',
                   data=data,
                   cookies=r1_cookie)

login_cookie = r2.cookies.get_dict()
print('r2.cookies:', r2.cookies)
print('login_cookie:', login_cookie)

# 第三次请求：以后的登录，拿着login_cookie就可以,比如访问一些个人配置
url = 'https://github.com/settings/emails'
r3 = requests.get(url, cookies=login_cookie)

# 需要这些步骤，带上cookie，直接访问时不行的
print('15655982512' in r3.text)  # True

# ==================
'''使用session自动处理cookie'''
session = requests.Session()
# 第一次请求
r1 = session.get('https://github.com/login')
authenticity_token = \
    re.findall(r'name="authenticity_token".*?value="(.*?)"', r1.text)[
        0]  # 从页面中拿到CSRF TOKEN

# 第二次请求：带着初始cookie和TOKEN发送POST请求给登录页面，带上账号密码
data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': 'python-yc',
    'password': 'yc13705676620'
}

r2 = session.post('https://github.com/session', data=data)
# 第三次请求
r3 = session.get('https://github.com/settings/emails')

print('15655982512' in r3.text)  # True

## 3.3、补充json
#没有指定请求头,#默认的请求头:application/x-www-form-urlencoed
requests.post(url='xxxxxxxx', data={'xxx': 'yyy'})

'''# 如果我们自定义请求头是application/json，并且用data传值，则服务端取不到值'''
requests.post(url='', data={'': 1},
              headers={
                  'content-type': 'application/json'
              })

'''默认的请求头：application/json'''
requests.post(url='', json={'': 1})
