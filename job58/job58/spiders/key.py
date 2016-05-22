# -*- coding: utf-8 -*-
import scrapy
from job58.items import Job58Item
from job58.utils import format

class KeySpider(scrapy.Spider):
    name = "key"
    allowed_domains = ["gz.58.com"]
    start_urls = (
        'http://www.gz.58.com/job/pn1/?key=化工',
    )

    def parse(self, response):
        for i in range(0, 70):
            parent_url = 'http://www.gz.58.com/job/pn'+str(i)+'/?key=化工'
            yield scrapy.http.Request(parent_url, callback=self.parseThird)

    def parseSecond(self, response):
        item = response.meta['item']
        item['company_name'] = format(response.xpath('//a[@class="companyName"]/text()').extract()[0])
        item['salary'] = response.xpath('//span[@class="salaNum"]/strong/text()').extract()[0]
        item['job_name'] = format(response.xpath('//div[@class="xq"]/ul/li[2]/div[@class="w380"]/text()').extract()[1])
        item['location'] = response.xpath('//div[@class="xq"]/ul/li[3]/span[2]/text()').extract()[0]
        item['degree'] = format(response.xpath('//div[@class="xq"]/ul/li[1]/div[@class="fl"]/text()').extract()[1])
        item['job_year'] = format(response.xpath('//div[@class="xq"]/ul/li[2]/div[@class="fl"]/text()').extract()[1])
        item['introduction'] = format(response.xpath('//div[@id="tabC"]/div[1]/div[1]').extract()[0])
        return item

    def parseThird(self, response):
        items = []
        urls = response.xpath('//a[@class="t"]/@href').extract()
        for i in range(0, len(urls)):
            item = Job58Item()
            item['url'] = urls[i]
            items.append(item)
        for item in items:
            yield scrapy.http.Request(item['url'], meta={'item': item}, callback=self.parseSecond)