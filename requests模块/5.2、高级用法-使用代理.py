# -*- coding: utf-8 -*-
# 官网链接: http://docs.python-requests.org/en/master/user/advanced/#proxies
# 代理设置：先发送请求给代理，然后由代理帮忙发送(封ip时最常见的事情)
import requests

proxies = {
    # 带用户名和密码的代理
    'http': 'http://user:passwd@proxy.huawei.com:8080',
    # 执行某个网址使用代理
    'https://www.baidu.com': 'http://localhost:9734',
    'https': 'https://localhost:9734'
}

rsp = requests.get('https://www.12306.cn',
                   proxies=proxies)

print(rsp.status_code)


"""迟滞socks代理，安装：pip install requests[socks]"""
proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:pass@host:port'
}

rsp = requests.get('https://www.12306.cn',
                   proxies=proxies)

print(rsp.status_code)
