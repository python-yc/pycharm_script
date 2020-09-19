# -*- coding: utf-8 -*-
'''
使用参数headers和params
其中：
requests的get或者post请求，返回的响应response获取方法;

content和text
content用于获取图片，返回二进制数据
text用于获取内容，返回的是unicode解码字符串
两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串
所以简而言之，.text是现成的字符串，.content还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码
'''

import requests

url = "https://fanyi.baidu.com/sug"

kw = {
    "wd": "小菜鸡"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/73.0.3683.86 Safari/537.36"
}

# rsp = requests.get(url, params=kw)

rsp = requests.get(url, params=kw, headers=headers)
# rsp = requests.post(url, data=kw)

print(rsp.text)
print(rsp.content, '###')
print(rsp.url)
print(rsp.encoding)
# print(rsp.status_code)
print(rsp.json())

