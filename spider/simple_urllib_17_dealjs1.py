# -*- coding: utf-8 -*-

from urllib import request, parse
import hashlib

def youdao(key):
    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    # 通过百度只是简单解决了{"errorCode":50}的问题，但不是根本，只是个例子，不想去深究了
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    # key = key
    # md5 = hashlib.md5()
    # md5.update(key)
    data = {
       "i": "girl",
       "from": "AUTO",
       "to": "AUTO",
       "smartresult": "dict",
       "client": "fanyideskweb",
       "salt": "15654886587107",
       "sign": "9b930a9aba3f895d8fdecdfaff53d46a",
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
       "Content-Length": "241",
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
    youdao("boy")  # 此处传参未生效

