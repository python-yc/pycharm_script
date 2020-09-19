# -*- coding: utf-8 -*-

from urllib import request, parse
import hashlib

'''
    # 盐值计算公式，从http的请求的response中获取值，然后利用在线代码格式化进行保存后(format.txt)搜索salt
    # salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
    # sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
    md5一种需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，
    第二个参数是输入的要查的单词
'''

def getSalt():
    '''
    salt公式是： "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
    把他翻译成python代码
    :return: 
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    #
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):
    sign = "fanyideskweb" + key + str(getSalt()) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)

    return sign

def youdao(key):
    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # 通过百度只是简单解决了{"errorCode":50}的问题，但不是根本，只是个例子，不想去深究了
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    salt = str(getSalt())
    data = {
       "i": key,
       "from": "AUTO",
       "to": "AUTO",
       "smartresult": "dict",
       "client": "fanyideskweb",
       "salt": str(salt),
       "sign": getSign(key, salt),
       "ts": "1565488658710",
       "bv": "d59c4e53e6e5b3de2a913eb58deea42a",
       "doctype": "json",
       "version": "2.1",
       "keyfrom": "fanyi.web",
       "action": "FY_BY_CLICKBUTTION"
    }

    # 参数data需要bytes格式
    data = parse.urlencode(data).encode()

    headers = {
       "Accept": "application/json, text/javascript, */*; q=0.01",
       # "Accept-Encoding": "gzip, deflate",    # 不想要gzip压缩，所以将此行注释即可
       "Accept-Language": "zh-CN,zh;q=0.9",
       "Connection": "keep-alive",
       "Content-Length": len(data),
       "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
       "Cookie": "OUTFOX_SEARCH_USER_ID=1115385938@10169.0.83; JSESSIONID=aaayQO-iKODlBh5xdz_Xw;OUTFOX_SEARCH_USER_ID_NCOO=1286522874.44671;___rl__test__cookies=1565488658703",
       "Host": "fanyi.youdao.com",
       "Origin": "http://fanyi.youdao.com",
       "Referer": "http://fanyi.youdao.com/",
       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36",
       "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':

    # 此处传参生效,是对simple_urllib_17_dealjs1.py进行改进而来
    youdao("boy")

