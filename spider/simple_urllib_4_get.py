# -*- coding: utf-8 -*-
from urllib import request, parse
'''
简单的小爬虫，注意数据要进行解码
学习parse的编码
'''

if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("Input your keyword:")

    # 要想使用data，需要使用字典结构
    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl, qs, sep="\n")

    # 打开相应url，把相应页面作为返回
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)

    # print(type(rsp))    # <class 'http.client.HTTPResponse'>
    # print(rsp)  # <http.client.HTTPResponse object at 0x0000000002E6E860>
    #
    # print("URL: {0}".format(rsp.geturl()))
    # print("########################")
    # print("Info: {0}".format(rsp.info()))
    # print("########################")
    #
    # # 如果函数getcode不添加括号，得到的是一个乱码 <bound method HTTPResponse.getcode of <http.client.HTTPResponse object at 0x0000000002943940>>
    # print("Code: {0}".format(rsp.getcode()))



    # 直接打印是一种b开头的结果（b'<!DOCTYPE html><html><head><noscript><meta http-eq.....）
    # bytes流，然后需要进行解码
    # html = rsp.read()
    # # print(type(html)) #<class 'bytes'>
    # # 对其进行解码
    # html = html.decode()     # decode中可以直接指定编码格式如："utf-8"
