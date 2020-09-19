# -*- coding: utf-8 -*-
"""
通用VIP电影解析网址：
http://api.xfsub.com/index.php?url=[播放地址或视频id]
如：对于绣春刀这个电影，我们只需要在浏览器地址栏输入：
http://api.xfsub.com/index.php?url=http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1
"""
"""
编写代码的时候注意一个问题，就是我们需要使用requests.session()保持我们的会话请求。
简单理解就是，在初次访问服务器的时候，服务器会给你分配一个身份证明。我们需要拿着这个身份证去继续访问，
如果没有这个身份证明，服务器就不会再让你访问。这也就是这个服务器的反爬虫手段，会验证用户的身份

编程思路：
用正则表达式匹配到key、time、url等信息。
根据匹配的到信息发POST请求，获得一个存放视频信息的url。
根据这个url获得视频存放的地址。
根据最终的视频地址，下载视频。

python3中urllib.request模块提供的urlretrieve()函数。urlretrieve()方法直接将远程数据下载到本地。

urlretrieve(url, filename=None, reporthook=None, data=None)

参数url：下载链接地址
参数filename：指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
参数reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
参数data：指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头
"""
import requests, re, json, sys
from bs4 import BeautifulSoup
from urllib import request

class GetVideo:
    def __init__(self, url):
        self.server = 'http://api.xfsub.com'
        self.api = 'http://api.xfsub.com/xfsub_api/?url='
        self.get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'
        self.url = url.split('#')[0]
        self.target = self.api + self.url
        self.session = requests.session()

    def get_key(self):
        """函数说明:获取key、time、url等参数
       内容类似这种：
       xfsub_api\/url.php?key=02896e4af69fb18f70129b6046d7c718&time=1505724557&url=http%3A%2F%2Fwww.iqiyi.com%2Fv_19rr7qhfg0.html&type=&xml=1
       Parameters:无
       Returns:无
        """
        req = requests.get(url=self.target)
        req.encoding = 'utf-8'
        # 使用正则表达式匹配结果，将匹配的结果存入info变量中
        self.info = json.loads(re.findall('"url.php",\ (.+),', req.text)[0])

    def get_url(self):
        """函数说明:获取视频地址
       Parameters:无
       Returns:video_url - 视频存放地址
        """
        data = {
            'time': self.info['time'],
            'key': self.info['key'],
            'url': self.info['url'],
            'type': ''
        }
        req = self.session.post(url=self.get_url_api, data=data)
        url = self.server + json.loads(req.text)['url']
        req = self.session.get(url)
        soup = BeautifulSoup(req.text, 'xml')
        video_url = soup.find('file').string
        return video_url

    def schedule(self, a, b, c):
        """函数说明:回调函数，打印下载进度
        Parameters:a b c - 返回信息
        Returns:无
        """
        per = 100.0 * a * b / c
        if per > 100:
            per = 1
        sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per,a*b,c) + '\r')
        sys.stdout.flush()

    def download_video(self, url, filename):
        """函数说明:视频下载
        Parameters:
            url - 视频地址
            filename - 视频名字
        Returns: 无
        """
        request.urlretrieve(url=url, filename=filename, reporthook=self.schedule)


if __name__ == '__main__':
    # url = 'https://www.iqiyi.com/v_19rsho7kz8.html?vfrm=pcw_home&vfrmblk=L&vfrmrst=712211_dianying_image5'
    url = 'http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1'
    gv = GetVideo(url)
    filename = '加勒比海盗'
    print('%s下载中：' % filename)
    gv.get_key()
    video_url = gv.get_url()
    print('  获取地址成功：%s' % video_url)
    gv.download_video(video_url, filename + '.mp4')
    print('\n下载完成！')

