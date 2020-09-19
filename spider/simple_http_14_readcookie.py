# -*- coding: utf-8 -*-

from urllib import request, parse
from http import cookiejar

# 创建filecookiejar的实例
filename = "C:/content.txt"
cookie = cookiejar.MozillaCookieJar()
cookie.load("C:/content.txt", ignore_discard=True, ignore_expires=True)
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def getHomePage():
    url = "http://www.renren.com/971863388/profile"

    # 如果已将执行了login函数，则opener自动已经包含相应的cookie信息
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open('C:/rsp.html', 'w') as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()




