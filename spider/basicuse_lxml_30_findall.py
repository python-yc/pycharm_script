# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re

url = "https://www.hao123.com/"

rsp = request.urlopen(url)

# 使用beautifulsoup就不需要对数据解码了
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

tags = soup.find_all(name='meta')
print(tags)

# 使用正则
tags = soup.find_all(re.compile('^me'))
print(tags)


