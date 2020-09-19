# -*- coding: utf-8 -*-
"""
此文档只为学习，实际执行结果可能有冲突，不理解，先学习再说。
与原文略有改动，可能是python使用的改动，理解即可
"""

# from bs4 import BeautifulSoup
# import requests
#
# if __name__ == '__main__':
#     server = 'https://www.biqukan.com/'
#     target = 'https://www.biqukan.com/1_1094/'
#     req = requests.get(url=target)
#     html = req.text
#     soup = BeautifulSoup(html, 'lxml')
#     div = soup.find_all('div', class_='listmain')
#     a_soup = BeautifulSoup(str(div[0]), 'lxml')
#     a = a_soup.find_all('a')
#     for each in a:
#         print(each.string, server + each.get('href'))

# ==========================================
#               正文
# ==========================================
"""
类说明：下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2019-12-22
"""
from bs4 import BeautifulSoup
import requests
import sys

class DownLoader:
    def __init__(self):
        self.server = 'https://www.biqukan.com/'
        self.target = 'https://www.biqukan.com/1_1094/'
        self.names = []     # 存放章节名
        self.urls = []      # 存放章节链接
        self.nums = 0       # 章节数

    def get_download_url(self):
        """
        函数说明：获取下载链接
        :return: 无
        """
        req = requests.get(url=self.target)
        html = req.text
        div_soup = BeautifulSoup(html, 'lxml')
        div = div_soup.find_all('div', calss_='listmain')
        a_soup = BeautifulSoup(str(div[0]), 'lxml')
        a = a_soup.find_all('a')
        self.nums = len(a[15:])     # 剔除不要的章节，并统计
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        """
        函数说明：获取章节内容
        :param target: 下载链接内容(string)
        :return: 章节内容(string)
        Modify: 2019-12-22
        """
        req = requests.get(url=target)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        texts = soup.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self, name, path, text):
        """
        函数说明：将爬取的文章内容写入文件
        :param name: 章节名称(string)
        :param path: 当前路径，小说保存名称(string)
        :param text: 章节内容(string)
        :return: 无
        """
        write_flag = True
        with open('path', 'a', encoding='utf-8') as f:
            f.write(name, '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = DownLoader()
    dl.get_download_url()
    print("《一念永恒》开始下载:")
    # for i in range(dl.nums):
    #     dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
    #     sys.stdout.write("已下载：%.3f%%" % float(i/dl.nums) + '\r')
    #     sys.stdout.flush()
    print("《一念永恒》下载完成.")
