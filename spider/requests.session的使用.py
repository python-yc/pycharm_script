# -*- coding: utf-8 -*-
import requests

UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
urls = ["https://www.baidu.com/s?wd=magdu", "https://www.baidu.com/s?wd=magdu"]

session = requests.Session()
# 此处同时可以重新了解一下with的使用形式
# 由于两个网址是一致的，一次会打印两次
# 这样也能发现每次登陆很多信息都会在变化，比如cookie
# 第二次的请求头ua会带上cookie
"""
requests的get或者post请求，返回的响应response获取方法：content和text
content用于获取图片，返回二进制数据
text用于获取内容，返回的是unicode解码字符串
两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串
所以简而言之，.text是现成的字符串，.content还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码
"""
with session:
    for url in urls:
        response = session.get(url,headers={'User-Agent': UserAgent})

        with response:
            print(type(response))
            # print(response.url)
            # print(response.status_code)
            print(response.text[:50])  # HTML的内容
            print('-'*30)
            print(response.cookies )    # 响应的cookie
            print('-' * 30)
            print(response.headers, '~~~~~~~~')
            print(response.request.headers)  # 请求头


