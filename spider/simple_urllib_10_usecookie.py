# -*- coding: utf-8 -*-
'''
use cookie to login the web_addr
'''

from urllib import request
import requests
from io import BytesIO
import gzip

if __name__ == '__main__':

    url = "https://www.douyu.com/directory/myFollow"

    headers = {
        "Cookie": "dy_did=812d8b0411336cecd604814900041501; smidV2=201904051449111bc6c86336a55b4671ae"
                  "bd455b742bcc004be08098e045cd0; loginrefer=pt_ee22iad3h25; Hm_lvt_e99aee90ec1b2106afe"
                  "7ec3b199020a7=1563802617,1563886517,1563971322,1565010344; PHPSESSID=qs4qbsdia2rg7v0c"
                  "j50mkms9g7; acf_did=812d8b0411336cecd604814900041501; acf_auth=2bccKwRJ9dDsWgqGnPO7uDS"
                  "jhNby6c0JmZjkYws1TRPm%2BHe8az9dhHU%2BWmOWYigiDZG5C8K%2BRQ1JFzD1kcZBpJkVF9sTe8R%2BVmCBj"
                  "sbvMqeENhjH3U85; wan_auth37wan=faa98c55130ehLygExGDPd99ABChP%2FqvwQGSsn3bByn%2B%2BOegN"
                  "rKcJa1ZzZmLkaESBnPFCWE6nzpMyqsTuqrTAdy8vuwJE8fGLgfZv4eFT0oE6b711g; acf_uid=33180099; a"
                  "cf_username=33180099; acf_nickname=Q15e591b06ef178a4f; acf_own_room=0; acf_groupid=1; "
                  "acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favanew%2Fface%2"
                  "F201802%2F25%2F19%2F023da7fe2562ea878e05a9ab414bfbb8_; acf_ct=0; acf_ltkid=32239453; ac"
                  "f_biz=1; acf_stk=d894ba36272e07e8; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1565422884"
    }

    req = request.Request(url,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read()
    buff = BytesIO(html)
    f = gzip.GzipFile(fileobj=buff)
    res = f.read
    print(res)

    # res = f.read().decode('utf-8')
    # print(res)

    # rsp = requests.get(url, headers=headers)
    #
    # html = rsp.text



