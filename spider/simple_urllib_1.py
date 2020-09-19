from urllib import request
'''
简单的小爬虫，注意数据要进行解码
简单的通过urllib的request模块获取网页并打印
'''

if __name__ == '__main__':
    url = "https://www.hao123.com/"
    # 打开相应url，把相应页面作为返回
    rsp = request.urlopen(url)

    # 直接打印是一种b开头的结果（b'<!DOCTYPE html><html><head><noscript><meta http-eq.....）
    # bytes流，然后需要进行解码
    html = rsp.read()
    # print(type(html)) #<class 'bytes'>

    # 对其进行解码
    html = html.decode()     # decode中可以直接指定编码格式如："utf-8"
    print(html)
