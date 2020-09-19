# -*- coding: utf-8 -*-
'''
使用代理访问百度网站
'''

from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baidu.com"

    # 基本使用步骤：
    # 1、设置代理地址
    proxy = {'http': '210.22.5.117:3128'}
    # 2、创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3、创建Opener
    opener = request.build_opener(proxy_handler)
    # 4、安装Opener
    request.install_opener(opener)

    # 现在访问url，则使用代理服务器
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode("GBK","ignore")
        print(html)
        with open("C:/a.txt", 'w+') as f:
            # write 遇到有不能写的就整个不写，使用writelines可以写一部分
            # 'gbk' codec can't encode character '\xbb' in position 29802: illegal multibyte sequence
            # 但是在解码内节加入.decode("GBK","ignore")，就不会出现格式问题了
            f.write(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)




