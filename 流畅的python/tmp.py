import requests

# url = "https://nj.meituan.com/meishi/api/poi/getPoiList?cityName=%E5%8D%97%E4%BA%AC&cateId=0"
url = 'http://sz.meituan.com/meishi/b32/pn1/'

headers = {
    "Accept": 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_lxsdk_cuid=1731e04178ac8-02aa34f43fec0b-376b4502-1fa400-1731e04178ac8; ci=55; rvct=55%2C1179; uuid=148619af18474ad48b47.1595138004.1.0.0; __mta=242580797.1593938475709.1593942186861.1595138005716.4; client-id=698a64d8-cb0f-4677-b6bd-620cf306df92; _lxsdk_s=17365a07bb5-3ea-08d-4f7%7C%7C7',
    'Host': 'nj.meituan.com',
    'Referer': 'https://nj.meituan.com/meishi/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

post_data = {
    'cityName': '南京',
    'cateId': 0,
    'areaId': 0,
    'sort': '',
    'dinnerCountAttrId': '',
    'page': 1,
    'userId': '',
    'uuid': '148619af18474ad48b47.1595138004.1.0.0',
    'platform': 1,
    'partner': 126,
    'originUrl': 'https://nj.meituan.com/meishi/',
    'riskLevel': 1,
    'optimusCode': 10,
    '_token': 'eJx1UE2PokAQ/S99XWJ3Q6Ng4gHUcVB7RHQQZzMHbHr4VFg+Fzbz36cnq4c9bFLJe/Xq5aWq/oDSCsAUI6QjJIGWl2AK8AiNxkACdSUmqq5iRUMyIhNdAuxfTZ3IEriU7gJMf2JdRhKRlfdvxRHCXwUjDb1LD04El4mob5clTCCq66KaQnhLRlce141/G7H8CgWvohiKLf5jACLhehQJAtM7+nesHz0V14iIKg5vgvF1lyUM10ay3EdeG5GN7R3Drkq93trNV5Eyj8LOoLTcKS43+7WVJEfTdPcLeDCzt4EX4w+Fdk+rk+G22CBLSJ5TLaQO5PWYD5Nmk5mbntYsVfoto01uG+XTqTir+TZYvfnnRbFHNozDPvv1ozn0LEh9Z47KijXaJTuskU8CY3N0E7/Ysg86vO4su6VVkFH1Mqy8352faUPsHhSiY1aaJz2wJ3Qrv7R8cNASyzDwXtrifM0hl3dMPC2nSrpIXs1np5vNwOcXwauVQQ=='
}


rsp = requests.get(url=url, headers=headers)
print(rsp.json())
print(rsp.status_code)
