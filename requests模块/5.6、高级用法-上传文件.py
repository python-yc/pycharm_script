# -*- coding: utf-8 -*-
import requests

files = {'file': open('a.jpg', 'rb')}

rsp = requests.post('http://httpbin.org/post', files=files)

print(rsp.status_code)
