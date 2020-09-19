# -*- coding: utf-8 -*-

from urllib import request
import ssl

if __name__ == '__main__':

    # 利用非认证上下文环境替换认证的上下文环境
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://www.12306.cn/mormhweb"

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    print(html)



