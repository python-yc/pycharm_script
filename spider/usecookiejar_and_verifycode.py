# -*- coding: utf-8 -*-

from urllib import request, parse
from http import cookiejar
import requests
from io import BytesIO
from PIL import Image


# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 安装管理器
request.install_opener(opener)

'''
当然，如果把上面这个生成的opener对象使用install_opener方法来设置为全局的，opener对象之后的每次访问都会带上这个cookie。
设置全局后既可以用urlopen()方法， 也可以用opener.open() ，不安装的话只能用opener.open()方法
'''

def login():
    '''
    负责首次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return: 
    '''

    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # data = {
    #     "email": "15655982512",
    #     "password": "Huawei@123",
    # }

    # imgbuf = requests.get(url).content
    # f = BytesIO()
    # f.write(imgbuf)
    # img = Image.open(f)
    # img.show()
    # vercode = input("Verification Code")
    # data["rkey"] = vercode

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email": "15655982512",
        "password": "Huawei@123",
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/971863388/profile"

    # 如果已将执行了login函数，则opener自动已经包含相应的cookie信息
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open('C:/rsp.html', 'w') as f:
        f.write(html)

    print(html)

if __name__ == '__main__':
    login()
    getHomePage()


