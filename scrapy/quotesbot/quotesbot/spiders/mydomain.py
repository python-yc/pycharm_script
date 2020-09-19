# -*- coding: utf-8 -*-

"""
此文件是在quotesbot的根目录下 cmd 窗口中执行
scrapy genspider mydomain mydomain.com  而得到的
"""
import scrapy


class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    allowed_domains = ['mydomain.com']
    start_urls = ['http://mydomain.com/']

    def parse(self, response):
        pass
