# -*- coding: utf-8 -*-
import requests
import re

# 第一次请求
r1 = requests.get('https://github.com/login')
r1_cookie = r1.cookies.get_dict()
# 从页面中拿到CSRF TOKEN
authenticity_token = \
    re.findall(r'name="authenticity_token".*?value="(.*?)"', r1.text)[0]

# 第二次请求：带着初始cookie和TOKEN发送POST请求给登录页面，带上账号密码
data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': 'python-yc',
    'password': 'yc13705676620'
}

"""测试一：没有指定allow_redirects=False， 则响应头中出现Location就跳转到新页面
r2代表刷新页面的response
"""
r2 = requests.post('https://github.com/session',
             data=data,
             cookies=r1_cookie)

print(r2.status_code) # 200
print(r2.url)   # 看到的时跳转后的页面 https://github.com/
print(r2.history) # 看到的是跳转前的response [<Response [302]>]
print(r2.history[0].text)   # 看到的是跳转前的response.text

'''测试二：指定allow_redirects=False,则响应头中几遍出现Location也不会跳转到新页面，
r3代表的仍是老页面的response'''
r3 = requests.post('https://github.com/session',
             data=data,
             cookies=r1_cookie,
             allow_redirects=False)

print(r3.status_code)   # 302
print(r3.url)   # https://github.com/session
print(r3.history)   # []
