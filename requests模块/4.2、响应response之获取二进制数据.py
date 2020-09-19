# -*- coding: utf-8 -*-
import requests

rsp = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1509868306530&di=712e4ef3ab258b36e9f4b48e85a81c9d&imgtype=0&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F11385343fbf2b211e1fb58a1c08065380dd78e0c.jpg')

with open('a.jpg', 'wb') as f:
    f.write(rsp.content)


'''获取二进制流  stream参数'''
# stream参数:一点一点的取,比如下载视频时,如果视频100G,用response.content然后一下子写到文件中是不合理的

rsp = requests.get('https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo-transcode/1767502_56ec685f9c7ec542eeaf6eac93a65dc7_6fe25cd1347c_3.mp4',
                   stream=True)

with open('b.mp4', 'wb') as f:
    for line in rsp.iter_content():
        f.write(line)
