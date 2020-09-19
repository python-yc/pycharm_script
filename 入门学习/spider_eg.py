#coding=utf-8
"""
此处不支持，未知
爬虫,也可以叫做网页蜘蛛（Web Spider），
如果把互联网比喻成一个蜘蛛网，那么Spider就是在网上爬来爬去的蜘蛛。
网络蜘蛛通过网页的链接地址来寻找网页，定向抓取我们想要的资源，并且可以下载/保存下来
"""

#举例：爬取新浪首页的图片,下载到本地
# 其中urlopen函数在urllib.request模块中；读取网页内容是添加上解码格式，decode('utf-8'),然后在这里就可以执行了
# import urllib
# from urllib.request import urlopen
# import re
# url="http://www.sina.com.cn/"
# page=urlopen(url)
# content=page.read().decode('utf-8')
# rg='data-src="(.+?\.(jpg|png))"'
# reg=re.compile(rg)
# find=reg.findall(content)
# print(find)
# j=0
# 有问题，懒得百度调试，太浪费时间，主要大致思路指导就好
# for i in find:
#     imgurl=i[0]
#     imgurl=re.sub('^//','http://',imgurl)  #将imgurl中开头的//替换为http://
#     print (imgurl)
#     with open("C:\\img\\%r.jpg" %j) as f:
#         f.write(imgurl)
#     j+=1
# print(j)

def ab():
    return 3,5
y = ab()
print(y)
