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
        print(
            '[Error]: Fail to get who care me in <qq_spider.py - get_cared_me func>...')
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
        print(
            '[Error]: Fail to get me care who in <qq_spider.py - get_me_cared func>...')
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


# 爬取好友信息
def download_friends_info(qq, t_qq, gtk, headers, faillog='./results'):
    url = 'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/user/cgi_userinfo_get_all?uin={}&vuin={}&fupdate=1&g_tk={}'
    url = url.format(t_qq, qq, gtk)
    res = requests.get(url, headers=headers)
    status = res.status_code
    if status != 200:
        print(
            '[Error]: Fail to get %s info in <qq_spider - download_friends_info func>...' % str(
                t_qq))
        f = open(os.path.join(faillog, '{}.fail'.format(qq)), 'a', encoding='utf-8')
        f.write(str(t_qq) + '\n')
        f.close()
        return None
    content = res.content
    content = content.decode('ascii', 'ignore')
    save_html(content, './results/{}'.format(qq), '{}_info.txt'.format(t_qq))
    return content


# 获取所有好友信息
def get_all_friends_info(qq, friends):
    friends_info_dict = {}
    for friend in friends:
        info_dict = parse_friends_info(qq, friend, datafile='./results')
        if info_dict is not None:
            friends_info_dict[friend] = info_dict
    return friends_info_dict


if __name__ == '__main__':
    username = 'qq number'
    password = 'qq password'
    qq, gtk, headers = cookie.get(username, password)
    get_cared(qq, gtk, headers)
    friends = read_cared(os.path.join('./results', qq, 'cared.list'))
    print('[Info]: Start to download info of %d friends...' % len(friends))
    for friend in friends:
        download_friends_info(qq, friend, gtk, headers)

    friends_info_dict = get_all_friends_info(qq, friends)
    '''
    # 性别分析
    boy, girl, other = count_sex(friendsInfoDict)
    data = [['boy', 'girl', 'other'], [boy, girl, other]]
    draw_pie(data, piename='QQ好友男女比')
    '''
    '''
    # 年龄分析
    data = count_age(friendsInfoDict)
    draw_bar(data, barname='QQ好友年龄分布')
    '''
    # 地区分布分析
    data = count_area(friends_info_dict, 'province')
    draw_map(data, map_name='QQ好友区域分布')
