# -*- coding: utf-8 -*-
import requests
import json

rsp = requests.get('http://httpbin.org/get')

res1 = json.loads(rsp.text) # 太麻烦

res2 = rsp.json()   # 直接获取json数据

print(res1 == res2) # True
print(res2)
