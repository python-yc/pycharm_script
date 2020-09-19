# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

"""
1	Python标准库	BeautifulSoup(html,’html.parser’)	Python内置标准库；执行速度快	容错能力较差
2	lxml HTML解析库	BeautifulSoup(html,’lxml’)	速度快；容错能力强	需要安装，需要C语言库
3	lxml XML解析库	BeautifulSoup(html,[‘lxml’,’xml’])	速度快；容错能力强；支持XML格式	需要C语言库
4	htm5lib解析库	BeautifulSoup(html,’htm5llib’)	以浏览器方式解析，最好的容错性	速度慢
"""

for i in range(1, 10):
    ret = requests.get(url='https://www.autohome.com.cn/news/%s/#liststart' % (i,))
    ret.encoding = ret.apparent_encoding
    soup = BeautifulSoup(ret.text, 'lxml')
    div = soup.find(name='div', attrs={'id': 'auto-channel-lazyload-article'})
    li_list = div._find_all(name='li')
    for li in li_list:
        h3 = li.find(name='h3')
        if not h3:
            continue
        p_text = li.find(name='p').text
        href = li.find(name='a').get('href')
        img = li.find(name='img').get('src')

        print('''
        新闻标题：%s
        新闻简介：%s
        新闻地址：%s
        新闻图片：%s
        ''' % (h3.text, p_text, 'https:' + href, 'https:' + img))
        ret_photo = requests.get(url='https:' + img)
        phtot_name = img.rsplit('__', 1)[-1]
        if not os.path.exists('download'):
            os.mkdir('download')
        with open('download/' + phtot_name, 'wb') as f:
            f.write(ret_photo.content)
