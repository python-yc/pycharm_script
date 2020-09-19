# -*- coding: utf-8 -*-

print()

"""
#建议在正式学习requests前，先熟悉下HTTP协议
https://www.cnblogs.com/liuqingzheng/p/10191056.html

介绍：使用requests可以模拟浏览器的请求，比起urllib，requests模块的api更加便捷（本质就是封装了urllib3）

### 注意：
requests库发送请求将网页内容下载下来以后，并不会执行js代码，
这需要我们自己分析目标站点然后发起新的request请求.
# 安装：pip3 install requests

get：获取资源
post：传输资源
put：更新资源
delete：删除资源
head：获得报文首部

get与post的区别：
1、get在浏览器回退时是无害的，而post会再次提交请求；
2、get请求会被浏览器主动缓存，而post不会，除非手动设置；
3、get请求参数会被完整保留在浏览器历史记录里，而post中的参数不会；
4、get请求在url中传送的参数长度是有限制的，而post没有限制；
5、get参数通过url传递，而post放在request body中。
"""

"""各种请求方式：常用的就是requests.get() 和 requests.post()"""
import requests

r = requests.get('https://api.github.com/events')

r = requests.post('http://httpbin.org/post', data={'key': 'value'})

r = requests.put('http://httpbin.org/put', data={'key': 'value'})

r = requests.delete('http://httpbin.org/delete')

r = requests.head('http://httpbin.org/get')

r = requests.options('http://httpbin.org/get')
