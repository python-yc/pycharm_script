# -*- coding: utf-8 -*-
import scrapy

class ToScrapeSpiderXPath(scrapy.Spider):
    name = "toscrape-xpath2"
    start_urls = [
        "http://quotes.toscrape.com/",
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract_first()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


