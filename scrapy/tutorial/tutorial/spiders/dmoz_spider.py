# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    # name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    name = "fanyi"
    allowed_domains = ["fanyi.baidu.com"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "https://fanyi.baidu.com/#en/zh/tutorial"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # TODO 未找到这个数据记录问题，可能不是这样表达
        # with open("test.txt", 'wb') as f:
        #     f.write(response.headers)
        #     f.write(response.xpath("/html/head/title/text()"))
        for sel in response.xpath("//div"):
            # title = sel.xpath('img/text()').extract()
            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # print(title, link, desc)
            item = DmozItem()
            item['title'] = sel.xpath('.//img/text()').extract()
            item['link'] = sel.xpath('.//a/@href').extract()
            item['desc'] = sel.xpath('.//p/text()').extract()
            yield item

"""
from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
       
        # The lines below is a spider contract. For more info see:
        # http://doc.scrapy.org/en/latest/topics/contracts.html
        # 
        # @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        # @scrapes name
        
        sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.css(
                'a > div.site-title::text').extract_first().strip()
            item['url'] = site.xpath(
                'a/@href').extract_first().strip()
            item['description'] = site.css(
                'div.site-descr::text').extract_first().strip()
            items.append(item)

        return items

"""
