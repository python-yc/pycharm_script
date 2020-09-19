# -*- coding: utf-8 -*-
'''
动态获取页面元素，对网页进行分析
获取网页信息时也利用了F12中的XHR方式查找数据
是用with方式
'''

from urllib import request
from urllib import parse
import json

ua = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

# jurl = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
# 这个数json数据，且上面的url可以进行拼接拿取，就是翻页的功能部分获取
jurl = 'https://movie.douban.com/j/search_subjects'

data = {
    # 这些数据可以从网页F12进行获取
    # XHR表示xml、http、request，找到对应的异步请求
    # type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
   "type": "movie",
   "tag": "热门",
   "page_limit": 10,
   "page_start": 10
}

req = request.Request('{}?{}'.format(jurl, parse.urlencode(data)), headers={
    'User-Agent': ua
})

# res = request.urlopen(req)
# 或者这样表达
with request.urlopen(req) as res:
    subjects = json.loads(res.read().decode('utf-8'))
    print(len(subjects))
    print(len(subjects['subjects']))
    print(subjects)

