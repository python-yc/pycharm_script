# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = "https://www.hao123.com/"

rsp = request.urlopen(url)

# 使用beautifulsoup就不需要对数据解码了
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())
# print("==" * 12)
titles = soup.select("title")
print(titles)
print(titles[0])

metas = soup.select("meta[content='always']")
print(metas)



