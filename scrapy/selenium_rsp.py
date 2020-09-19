# -*- coding: utf-8 -*-
'''
class MyMiddWare(object):
    def process_request(self):
        driver = webdriver.Chrome()
        html = driver.page_source
        driver.quit()
        return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)
# 使用selenium后就不会调用Downloader下载器
'''