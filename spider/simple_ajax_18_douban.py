# -*- coding: utf-8 -*-

'''
爬豆瓣电影动态数据
了解ajax
'''
from urllib import request
import json

url = "https://movie.douban.com/j/search_tags?type=movie&source=index"

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)

