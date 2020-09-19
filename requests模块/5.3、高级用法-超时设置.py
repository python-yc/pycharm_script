# -*- coding: utf-8 -*-
# 超时设置
# 两种超时:float or tuple
# timeout=0.1 #代表接收数据的超时时间
# timeout=(0.1,0.2)#0.1代表链接超时  0.2代表接收数据的超时时间
import requests

rsp = requests.get('https://www.baidu.com', timeout=2)
print(rsp.status_code)

# rsp = requests.get('https://www.baidu.com', timeout=0.02)
# print(rsp.status_code)
