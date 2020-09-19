# -*- coding: utf-8 -*-
import requests

rsp = requests.get('http://www.jianshu.com')

'''response属性'''
print(rsp.text)
print(rsp.content)

print(rsp.status_code)
print(rsp.headers)

print(rsp.cookies)
print(rsp.cookies.get_dict())
print(rsp.cookies.items())

print(rsp.url)
print(rsp.history)

print(rsp.encoding)

# 关闭：rsp.close()
from contextlib import closing
with closing(requests.get('xxx', stream=True)) as rsp:
    for line in rsp.iter_content():
        pass
