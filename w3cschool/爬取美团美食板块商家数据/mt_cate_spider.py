# -*- coding: utf-8 -*-
# 美团美食板块商家信息爬取脚本
# 作者：Charles
# 公众号：Charles的皮卡丘
import json
import requests
import random
import urllib
import cookies
import time
from openpyxl import Workbook
import win_unicode_console
win_unicode_console.enable()


# 获得城市地址
def get_city_url(city_name):
    f = open('cities_url.json', 'r', encoding='utf-8')
    cities_url = json.load(f)
    f.close()
    idx = cities_url['city_name'].index(city_name)
    return cities_url['city_url'][idx]


# city_url = get_city_url('南京')
# print(city_url)

# 获得 cookies 值
def get_cookies():
    cookie = cookies.cookies[random.randint(0, len(cookies.cookies) - 1)]
    return cookie


# 获得商家数据
def get_data(city_name, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36',
        'Referer': 'https://nj.meituan.com/meishi/',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q = 0.9',
        'Connection': 'keep-alive',
        'Cookie': get_cookies()
    }
    all_data = []
    num = 1
    while True:
        print('[Info(Data)]: Getting Page %s' % num)
        num += 1
        page_url = url + 'api/poi/getPoiList?cityName={}&page={}'.format(
            urllib.parse.quote(city_name), num)
        print('page_url:',page_url)
        try:
            res = requests.get(page_url, headers=headers)
        except:
            print('[Info]: %s Requests Error...' % page_url)
            continue
        print('res:',res)
        data_list = res.json()['data']['poiInfos']
        if len(data_list) < 1:
            print('[Info]: All data has getted...')
            break
        for dl in data_list:
            # 店名
            name = dl['title']
            # 评分
            score = dl['avgScore']
            # 评论数量
            comment_num = dl['allCommentNum']
            # 均价
            price = dl['avgPrice']
            # 地址
            addr = dl['address']

            all_data.append([name, score, comment_num, price, addr])
        # 随机休息一段时间，为了做反爬虫处理
        time.sleep(random.randint(1, 5))
    return all_data


# 结果保存到 excel中   merchant_list:商家列表
def save_to_excel(merchant_list, excel_name):
    wb = Workbook()
    ws = wb.active
    ws.append(['店名', '评分', '评论数量', '均价', '地址'])
    for ml in merchant_list:
        try:
            ws.append([ml[0], ml[1], ml[2], ml[3], ml[4]])
        except:
            print('[Warning]: A merchant lost...')
            continue
    wb.save('./results/' + excel_name + '.xlsx')
    print('[Info]: Data saved to excel successfully...')


def main():
    # 选择你想要爬取的城市
    city_choice = input('Enter the city name(In Chinese):')
    try:
        city_url = get_city_url(city_choice)
    except:
        print('[Error]: City Name Error...')
        return None
    city_cate_url = city_url + '/meishi/'
    print('city_cate_url:', city_cate_url)
    # 开始爬取数据
    all_data = get_data(city_choice, city_cate_url)
    # 将数据存储到 Excel中
    save_to_excel(all_data, city_choice)


if __name__ == '__main__':
    main()
