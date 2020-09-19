# -*- coding: utf-8 -*-

from urllib import request, parse
from http import cookiejar

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

def login():
    '''
    负责首次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return: 
    '''

    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email": "15655982512",
        "password": "Huawei@123"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    '''
    login执行结束之后，会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    login()

    print(cookie)
    print(type(cookie))
    for item in cookie:
        print(item)
        # 查看cookie的属性
        for i in dir(item):
            print(i)



