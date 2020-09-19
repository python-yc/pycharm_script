# -*- coding: utf-8 -*-
import requests

url = "http://music.taihe.com/top/dayhot"

rsp = requests.get(url)
rsp.encoding = 'utf-8'

print(rsp.content)


