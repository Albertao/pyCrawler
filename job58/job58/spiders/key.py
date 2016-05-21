# -*- coding: utf-8 -*-
import scrapy
#from job58

class KeySpider(scrapy.Spider):
    name = "key"
    allowed_domains = ["gz.58.com"]
    start_urls = (
        'http://www.gz.58.com/job/?key=化工',
    )

    def parse(self, response):
        urls = []
        urls = response.xpath('//a[@class="t"]/@href').extract()
