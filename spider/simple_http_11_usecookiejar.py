# -*- coding: utf-8 -*-

from urllib import request, parse
from http import cookiejar
import json

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

request.install_opener(opener)

def login():
    '''
    负责首次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return: 
    '''

    # 此url需要从登录form的action属性中提取；末尾一定要加/
    url = "http://www.renren.com/PLogin.do/"

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

def getHomePage():
    # url = "http://www.renren.com/971863388/profile"

    url = "http://huodong.renren.com/common/activity/suggest/getSuggestions?offset=0&limit=20"
    # 如果已将执行了login函数，则opener自动已经包含相应的cookie信息
    rsp = opener.open(url)

    # ret = rsp.read().decode()
    ret = rsp.read()
    ret = json.loads(ret)

    # with open('C:/rsp.html', 'w') as f:
    #     f.write(html)

    print(ret)
    print("##")
    print(type(ret))
    print(ret["suggestArray"][19])

if __name__ == '__main__':
    login()
    getHomePage()


