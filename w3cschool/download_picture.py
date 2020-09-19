# -*- coding: utf-8 -*-
import requests
import json
import sys, time

class GetPhoto:
    def __init__(self):
        self.photo_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.target = 'https://unsplash.com/napi/photos/0Jt5a_HB5kM/related'
        self.headers = {'authority': 'unsplash.com'}

    def get_ids(self):
        """
        函数说明：获取图片ID
        :return: 无
        """
        req = requests.get(url=self.target)
        html = json.loads(req.text)
        next_page = html['next_page']
        for each in html['photo']:
            self.photo_id.append(each['id'])
        time.sleep(1)
        for i in range(5):
            req = requests.get(url=next_page, headers=self.headers, verify=False)
            html = json.loads(req.text)
            next_page = html['next_page']
            for each in html['photo']:
                self.photo_id.append(each['id'])
            time.sleep(1)

    def download(self, photo_id, filename):
        """
        函数说明：图片下载
        :param photo_id: 
        :param filename: 
        :return: 
        """
        ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        headers = {'user-agent': ua}
        target = self.download_server.replace('xxx', photo_id)
        with requests.get(url=target,steam=True,varify=False, headers=headers) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = GetPhoto()
    print("获取图片的连接中")
    gp.get_ids()
    print("图片下载中：")
    # for i in range(len(gp.photo_id)):
    #     print("正在下载第{}张图片".format(i+1))
    #     gp.download(gp.photo_id[i], (i+1))
