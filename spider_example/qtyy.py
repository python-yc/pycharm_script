# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
# 这个可以爬取了，但是文件报服务器未授权，爬取失败，还有就是主页面未找到关于每页的请求

url = "http://www.htqyy.com/top/hot"
base_url = "http://f2.htqyy.com/play7/"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.36"
              "83.86 Safari/537.36"
}

content = requests.get(url).text
soup = BeautifulSoup(content, 'lxml')
# print(soup)
# ids = soup.select('#musicList > li:nth-child(1) > span.title')

spans = soup.find_all('span', {'class': 'title'})
# print(spans[0])

ids = []
names = []
for i in spans:
    id = i.a.get('href').split('/')[2]
    ids.append(id)
    name = i.text
    names.append(name)
print(ids)
print(names)
# print(ids[0].a.get('href').split('/')[2])

for i in range(len(ids)-1):
    if ids[i] and names[i]:
        rsp = requests.get(base_url+str(ids[i])+"mp3/8", headers=headers).content
        # with open('D:/qtyy/'+names[i]+'.mp3', 'wb') as f:
        print(rsp)
        #     f.write(rsp)
            # print("it is ok!")
    else:
        print(ids[i], names[i])
else:
    print("It's over!")

