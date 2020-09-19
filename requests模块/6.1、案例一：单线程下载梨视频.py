# -*- coding: utf-8 -*-
import requests
import re
import time
"""
本来呢: ^只匹配字符串的开头，$只匹配字符串结尾，.不匹配换行符.
re.S做的事情是: 让.也匹配换行符
re.M做的事情是: 让^匹配每行的开头，$匹配每行的结尾
re.I表示不区分大小写
"""


def get_page(url):
    try:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            return rsp.text
    except Exception as e:
        print('error here:', e)


def get_detail(index_page):
    # print('in get_detail')
    '''
    https://www.pearvideo.com/class="categoryem">
            <div class="vervideo-bd">
                <a href="video_1687624"
    '''
    # re.S 把上面一部分表示成一个字符串，对换行符也进行匹配
    urls = re.findall('class="categoryem".*?href="(.*?)"', index_page, re.S)
    # print(urls)
    # print(type(urls))
    for url in urls:
        yield 'https://www.pearvideo.com/' + url


def pase_detail(detail_page):
    down_url = re.findall('srcUrl="(.*?)"', detail_page, re.S)[0]
    # print(down_url)
    return down_url


def get_movie(url):
    rsp = requests.get(url)
    with open('movie/%s.mp4' % str(time.time()), 'wb') as f:
        for line in rsp.iter_content():
            f.write(line)
        print('下载成功.')


if __name__ == '__main__':
    index_page = get_page('https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=24')
    # print(index_page)
    urls = get_detail(index_page)
    # print('start')
    print(next(urls))
    # for i in urls:
    #     print(i)
    for url in urls:
        print(url)
        detail_page = get_page(url)
        mp4_url = pase_detail(detail_page)
        print(mp4_url)
        # get_movie(mp4_url)
