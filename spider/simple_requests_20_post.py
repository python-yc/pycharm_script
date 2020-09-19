# -*- coding: utf-8 -*-
from urllib import request, parse
import json
import requests

"""
pst与get的对比
"""

baseurl = 'https://fanyi.baidu.com/sug'

# 存放用来授权form的数据，一定是###dict###格式
data = {
    # girl是翻译输入的内容，应该是由用户输入，此处使用硬编码
    "kw": "girl"
}


rsp = requests.post(baseurl, data=data)

print(rsp.text)
print(rsp.json())


print("==" * 12)

rsp = requests.get(baseurl, data=data)

print(rsp.text)
print(rsp.json())

