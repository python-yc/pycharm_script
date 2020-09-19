# -*- coding: utf-8 -*-
import requests
import re
import time
from concurrent.futures import ThreadPoolExecutor
'''
RuntimeError: cannot schedule new futures afterinterpreter shutdown
暂时了解有限，这个不能正常运行，不追究了，学习形式即可

# Future: 未来对象/task 返回容器
# submit之后会返回future这个对象，这个时候任务是没有完成的，但是可能在将来某个时刻完成，所以叫未来对象
# task执行结果/执行状态，都会放在future对象（task 返回容器）中。如何更新这些结果/状态，何时更新？
'''

pool = ThreadPoolExecutor(50)


def get_page(url):
    print('get_page: ulr-->', url)
    try:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            return rsp.text
    except Exception as e:
        print(e)


def pase_index(index_page):
    index_page = index_page.result()
    # print('index_page:', index_page)
    urls = re.findall('class="categoryem".*?href="(.*?)"', index_page, re.S)
    print(urls)
    for url in urls:
        next_url = 'https://www.pearvideo.com/' + url
        try:
            pool.submit(get_page, next_url).add_done_callback(pase_detail)
        except RuntimeError:
            print('RuntimeError: cannot schedule new futures afterinterpreter shutdown')
        else:
            print('okokok')


def pase_detail(detail_page):
    detail_page = detail_page.result()
    down_url = re.findall('srcUrl="(.*?)"', detail_page, re.S)[0]
    pool.submit(get_movie, down_url)


def get_movie(url):
    print(url)
    # rsp = requests.get(url)
    # with open('movie/%s.mp4' % str(time.time()), 'wb') as f:
    #     f.write(rsp.content)
    #     print('下载成功。')


if __name__ == '__main__':
    for i in range(5):
        url = 'https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=%s' % (
                    (i + 1) * 12)
        pool.submit(get_page, url).add_done_callback(pase_index)
