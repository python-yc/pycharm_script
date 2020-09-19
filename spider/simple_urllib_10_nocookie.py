# -*- coding: utf-8 -*-
'''
没有cookie
遇到问题后此网址解决
https://blog.csdn.net/hj_xy_0705/article/details/85011072
'''
from urllib import request
from io import BytesIO
import gzip

if __name__ == '__main__':

    url = "http://www.renren.com/PLogin.do"


    rsp = request.urlopen(url)
    html = rsp.read().decode()
    with open('C:/a.txt', 'w') as f:
        f.write(html)
    print(html)

    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte

    # # 方法一：
    # buff = BytesIO(html)
    # f = gzip.GzipFile(fileobj=buff)
    # res = f.read().decode('utf-8')

    # print(res)

    # 方法二：
    import requests

    r = requests.get(url)

    # print(r.text)

