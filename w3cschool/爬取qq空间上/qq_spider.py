# -*- coding: utf-8 -*-
# QQ空间爬虫
# 作者: Charles
# 公众号: Charles的皮卡丘
import init
import cookie
import requests
import re
from utils import *

# 谁在意我
def get_cared_me(qq, gtk, headers):
    url = 'https://h5.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin={}&do=1&rd=0.11376390567557748&fupdate=1&clean=0&g_tk={}'
    url = url.format(qq, gtk)
    res = requests.get(url, headers=headers)
    status = res.status_code
    if status != 200:
        print('[Error]: Fail to get who care me in <qq_spider.py - get_cared_me func>...')
        exit(-1)
    content = res.content
    save_html(content, './resutls/{}'.format(qq), 'cared_me.txt')
    return content


# 我在意谁
def get_me_cared(qq, gtk, headers):
    url = 'https://h5.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin={}&do=1&rd=0.11376390567557748&fupdate=1&clean=0&g_tk={}'
    url = url.format(qq, gtk)
    res = requests.get(url, headers=headers)
    status = res.status_code
    if status != 200:
        print('[Error]: Fail to get me care who in <qq_spider.py - get_me_cared func>...')
        exit(-1)
    content = res.content
    save_html(content, './resutls/{}'.format(qq), 'me_cared.txt')
    return content


# 获得我关心谁/谁关心我信息
def get_cared(qq, gtk, headers, save_file='./results/cared.list'):
    care_me = get_cared_me(qq, gtk, headers)
    friend1 = re.findall(r'"uin":(.*?),', str(care_me))
    me_cared = get_me_cared(qq, gtk, headers)
    friend2 = re.findall(r'"uin":(.*?),', str(me_cared))
    try:
        f = open(save_file, 'w')
    except:
        import init
        f = open(save_file, 'w')
    f.write('CaredMe:\n')
    for friend in friend1:
        friend = friend.strip()
        if friend:
            f.write(str(friend) + ' ')
    f.write('\n\n\n')
    f.write('MeCared:\n')
    for friend in friend2:
        friend = friend.strip()
        if friend:
            f.write(str(friend) + ' ')
    print('[Info]: Get care and cared successfully, save to %s...' % save_file)


if __name__ == '__main__':
    username = 'qq number'
    password = 'qq password'
    qq, gtk, headers = cookie.get(username, password)
    get_cared(qq, gtk, headers)
