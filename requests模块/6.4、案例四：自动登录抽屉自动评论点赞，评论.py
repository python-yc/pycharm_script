# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    # 'accept-language': 'zh-CN,zh;q=0.9'
}

data = {
    'phone': '8618953675221',
    'password': 'lqz123',
    'oneMonth': '1'
}

'''打开抽屉首页'''
ret = requests.get(url='https://dig.chouti.com/', headers=headers)
# print(ret.text)
cookie = ret.cookies.get_dict()
print(cookie)

'''登录抽屉'''
ret_login = requests.post(url='https://dig.chouti.com/login', headers=headers,
                          data=data, cookies=cookie)

# print(ret_login.text)
# print(ret_login.cookies.get_dict())
# https://dig.chouti.com/link/vote?linksId=21055766
# ret_post = requests.post(url='https://dig.chouti.com/link/vote?linksId=21055766',
#                          headers={
#                              'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
#                          },
#                          cookies=coo
#                          )
# print(ret_post.text)

for i in range(2, 3):
    ret_index = requests.get(url='https://dig.chouti.com/all/hot/recent/%s'%i, headers=headers)
    soup = BeautifulSoup(ret_index.text, 'html.parser')
    div = soup.find(name='div', attrs={'id': 'content-list'})
    # print(div)
    item_list = div.find_all(name='div', attrs={'class': 'item'})
    # 点赞
    for item in item_list:
        part2_div = item.find(name='div', attrs={'class': 'part2'})
        nid = part2_div.get('share-linkid')
        print(nid)
        time.sleep(0.5)
        ret_post = requests.post(url='https://dig.chouti.com/link/vote?linksId=%s' % nid, headers=headers,
                                 cookies=cookie)
        print(ret_post)

# 给文章评论
ret_post = requests.post(url='https://dig.chouti.com/comments/create', headers=headers,
                         cookies=cookie,
                         data={
                             'jid': 'cdu_53207078460',
                             'linkId': '21061426',
                             'isAssent': '写的真好',
                             'sortType': 'score'
                         })
