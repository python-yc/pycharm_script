# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)

# 使用beautifulsoup就不需要对数据解码了
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs4自动转码
content = soup.prettify()
print(content)


