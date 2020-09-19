# -*- coding: utf-8 -*-
#异常处理
import requests
from requests.exceptions import * #可以查看requests.exceptions获取异常类型

try:
    r = requests.get('http://www.baidu.com', timeout=0.001)
except ReadTimeout:
    print('=======:')
except ConnectionError: # 网络不通
    print('------')
except Timeout:
    print('aaaaaa')
except RequestException:
    print('Error')

