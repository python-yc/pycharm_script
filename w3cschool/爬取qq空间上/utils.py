# -*- coding: utf-8 -*-
# 一些工具函数
"""
（1）第一次获取cookie之后将其保存下来，下次再登录之前先试试保存的cookie有没有用，有用直接使用就可以了，这样可以进一步节省时间。

（2）抓包分析过程中，可以发现抓取QQ空间数据所需请求的链接都包含g_tk这个参数，这个参数实际上是使用cookie中的skey参数计算获得的
"""
import os
import re


# 保存requests.content/text
def save_html(content, save_file, filename):
    if not os.path.exists(save_file):
        os.mkdir(save_file)
    f = open(os.path.join(save_file, filename), 'w')
    f.write(str(content))
    f.close()


# 保存cookie
def save_cookie(cookie, save_file='./data'):
    if not os.path.exists(save_file):
        print('[Warning]: %s inexistence, create new one...' % save_file)
        os.mkdir(save_file)
    f = open(os.path.join(save_file, 'cookie.info'), 'w')
    f.write(cookie)
    f.close()


# 读取cookie
def read_cookie(data_file='./data'):
    if not os.path.exists(data_file):
        print(
            '[Warning]: %s inexistence in <utils.py - read_cookie func>...' % data_file)
        return None
    txtpath = os.path.join(data_file, 'cookie.info')
    if not os.path.isfile(txtpath):
        print(
            '[Warning]: %s inexistence in <utils.py - read_cookie func>...' % txtpath)
        return None
    with open(txtpath, 'r') as f:
        cookie = f.read().strip()
    return cookie if cookie else None


# 获得Headers
def get_header(cookie=None):
    if cookie:
        headers = {
            "accept-language": "zh-CN,zh;q=0.9",
            "accept-encoding": "gzip, deflate, sdch, br",
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
            "cookie": cookie
        }
    else:
        headers = {
            "accept-language": "zh-CN,zh;q=0.9",
            "accept-encoding": "gzip, deflate, sdch, br",
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }
    return headers


# 获得 gtk
def get_gtk(skey):
    thash = 5381
    for c in skey:
        thash += (thash << 5) + ord(c)
    return thash & 2147483647


# 获得 skey
def get_skey(cookie):
    item = re.findall(r'p_skey=(.*?);', cookie)
    return item[0] if len(item) > 0 else None
