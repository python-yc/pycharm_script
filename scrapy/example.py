# -*- coding: utf-8 -*-
"""
此处只是一部分讲解，具体课堂为看到，自己百度查找相关scrapy的案例
"""
import random
import base64

# 从settings设置文件中导入值
from settings import USER_AGENTS
from settings import PROXIES
# 随机的User-Agent

class RandonmUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", useragent)

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            request.meta['proxy'] = "http://" + proxy['ip_port']
        else:
            # 对账户密码进行base64编码转换
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            # 对应到代理服务的命令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
            request.meta['proxy'] = "http://" + proxy['ip_prot']

'''
- 设置settings的相关代码
    USER_AGENTS = {
        # 多个真实的user_agent
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        ......,
    }
    
    PROXIES = {
        {'IP_PORT': '111.8.60.66：8123', 'user_passwd': 'user1:pass1'},
        {'IP_PORT': '111.8.61.67：8123', 'user_passwd': 'user2:pass2'},
        ......,
    }
'''




