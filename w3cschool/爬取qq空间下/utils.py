# -*- coding: utf-8 -*-
# 一些工具函数
"""
（1）第一次获取cookie之后将其保存下来，下次再登录之前先试试保存的cookie有没有用，有用直接使用就可以了，这样可以进一步节省时间。

（2）抓包分析过程中，可以发现抓取QQ空间数据所需请求的链接都包含g_tk这个参数，这个参数实际上是使用cookie中的skey参数计算获得的
"""
import os
import re
import time
import datetime

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


"""以下爬取qq空间下为新加"""
# 读取我关心和关心我的好友QQ
def read_cared(data_file):
    friends = []
    f = open(data_file, encoding='utf-8')
    for line in f:
        if line:
            try:
                int(line[0])
            except:
                continue
            friend = line.split(' ')
            for fri in friend:
                if fri not in friends:
                    friends.append(fri)
    return friends


# 画柱状图
def draw_bar(data, mark_point=["min", "max"], bar_name=None):
    from pyecharts import Bar
    if bar_name is not None:
        bar = Bar(bar_name)
    else:
        bar = Bar()
    try:
        bar.add('', data[0], data[1], mark_point=mark_point)
    except:
        print('[Error]: Arguments format error in <utils.py - draw_bar func>...')
        return None
    if bar_name is None:
        bar_name = 'results'
    bar.render('%s.html' % bar_name)


# 画饼图
def draw_pie(data, pie_name=None):
    from pyecharts import Pie
    if pie_name is not None:
        pie = Pie(pie_name)
    else:
        pie = Pie()
    try:
        pie.add('', data[0], data[1], is_label_show=True)
    except:
        print('[Error]: Arguments format error in <utils.py - draw_pie func>...')
        return None
    if pie_name is None:
        pie_name = 'resutls'
    pie.render('%s.html' % pie_name)


# 画地图
def draw_map(data, map_name=''):
    from pyecharts import Map
    map_ = Map(map_name, width=1200, height=600)
    try:
        map_.add('', data[0], data[1], maptype='china', is_visualmap=True,
                 visual_text_color='#000')
    except:
        print(
            '[Error]: Arguments format error in <utils.py - draw_map func>...')
        return None
    if map_name is '':
        mapname = 'results'
    map_.render('%s.html' % mapname)


# 性别统计
def count_sex(friends_info_dict):
    boy = 0
    girl = 0
    other = 0
    for key in friends_info_dict:
        try:
            if friends_info_dict[key]['sex'] == '2':
                girl += 1
            elif friends_info_dict[key]['sex'] == '1':
                boy += 1
            else:
                other += 1
        except:
            other += 1
    return boy, girl, other


# 年龄统计
def count_age(friends_info_dict):
    age_dict = {}
    for key in friends_info_dict:
        try:
            birth_year = friends_info_dict[key]['birthyear']
        except:
            birth_year = ''
        if birth_year == '' or birth_year =='0':
            age_dict['other'] = age_dict.get('other', 0) + 1
        else:
            age_dict[birth_year] = age_dict.get(birth_year, 0) + 1
    items = sorted(age_dict.items(), key=lambda x: x[0], reverse=True)
    counts = []
    ages = []
    for item in items:
        birth_year = item[0]
        count = item[1]
        if birth_year != 'other':
            age = datetime.datetime.now().year - int(birth_year)
            ages.append(age)
            counts.append(count)
        else:
            ages.append('Unkown')
            counts.append(count)
    return [ages, counts]


# 地区统计
def count_area(friends_info_dict, area_type):
    area_dict = {}
    for key in friends_info_dict:
        try:
            area = friends_info_dict[key][area_type]
        except:
            area = ''
        if area == '':
            area = 'Unkown'
        area_dict[area] = area_dict.get(area, 0) + 1
    return [list(area_dict.keys()), list(area_dict.values())]


# 解析好友信息
def parse_friends_info(qq, t_qq, datafil='./results'):
    info_txt = os.path.join(datafil, qq, t_qq + '_info.txt')
    if not os.path.exists(info_txt):
        return None
    info_dict = {}
    with open(info_txt, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 昵称
            if line.startswith('"nickname":'):
                nickname = re.findall(r'"nickname":"(.*?)",', line)[0]
                info_dict['nickname'] = nickname
                continue
            # 空间名
            elif line.startswith('"spacename":'):
                spacename = re.findall(r'"spacename":"(.*?)",', line)[0]
                info_dict['spacename'] = spacename
                continue
            # 空间简介
            elif line.startswith('"desc":'):
                desc = re.findall(r'"desc":"(.*?)",', line)[0]
                info_dict['desc'] = desc
                continue
            # 空间签名
            elif line.startswith('"signature":'):
                signature = re.findall(r'"signature":"(.*?)",', line)[0]
                info_dict['signature'] = signature
                continue
            # 性别
            elif line.startswith('"sex":'):
                sex = re.findall(r'"sex":(.*?),', line)[0]
                info_dict['sex'] = sex
                continue
            # 出生年
            elif line.startswith('"birthyear":'):
                birthyear = re.findall(r'"birthyear":(.*?),', line)[0]
                info_dict['birthyear'] = birthyear
                continue
            # 出生月日
            elif line.startswith('"birthday":'):
                birthday = re.findall(r'"birthday":"(.*?)",', line)[0]
                info_dict['birthday'] = birthday
                continue
            # 血型
            elif line.startswith('"bloodtype":'):
                bloodtype = re.findall(r'"bloodtype":(.*?),', line)[0]
                info_dict['bloodtype'] = bloodtype
                continue
            # 星座
            elif line.startswith('"constellation":'):
                constellation = re.findall(r'"constellation":(.*?),', line)[0]
                info_dict['constellation'] = constellation
                continue
            # 国家
            elif line.startswith('"country":'):
                country = re.findall(r'"country":"(.*?)",', line)[0]
                info_dict['country'] = country
                continue
            # 省
            elif line.startswith('"province":'):
                province = re.findall(r'"province":"(.*?)",', line)[0]
                info_dict['province'] = province
                continue
            # 城市
            elif line.startswith('"city":'):
                city = re.findall(r'"city":"(.*?)",', line)[0]
                info_dict['city'] = city
                continue
            # 家乡国
            elif line.startswith('"hco":'):
                hco = re.findall(r'"hco":"(.*?)",', line)[0]
                info_dict['hco'] = hco
                continue
            # 家乡省
            elif line.startswith('"hp":'):
                hp = re.findall(r'"hp":"(.*?)",', line)[0]
                info_dict['hp'] = hp
                continue
            # 家乡城
            elif line.startswith('"hc":'):
                hc = re.findall(r'"hc":"(.*?)",', line)[0]
                info_dict['hc'] = hc
                continue
            # 婚否
            elif line.startswith('"marriage":'):
                marriage = re.findall(r'"marriage":(.*?),', line)[0]
                info_dict['marriage'] = marriage
                continue
            # 职业
            elif line.startswith('"career":'):
                career = re.findall(r'"career":"(.*?)",', line)[0]
                info_dict['career'] = career
                continue
            # 公司
            elif line.startswith('"company":'):
                company = re.findall(r'"company":"(.*?)",', line)[0]
                info_dict['company'] = company
                continue
            # 最后修改时间
            elif line.startswith('"ptimestamp":'):
                ptimestamp = re.findall(r'"ptimestamp":(.*?)}', line)[0]
                if ptimestamp != '':
                    temp = time.localtime(float(ptimestamp))
                    createtime = time.strftime('%Y-%m-%d %H:%M:%S', temp)
                else:
                    createtime = ''
                info_dict['createtime'] = createtime
                continue
    return info_dict
