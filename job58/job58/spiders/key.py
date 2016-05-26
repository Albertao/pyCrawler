# -*- coding: utf-8 -*-
import scrapy
from job58.items import Job58Item
from job58.utils import format

class KeySpider(scrapy.Spider):
    name = "key"
    allowed_domains = ["gz.58.com"]
    start_urls = []

    def __init__(self, keyword="化工", page=70,  *a, **kw):
        for i in range(0, int(page)):
            self.start_urls.append('http://www.gz.58.com/job/pn'+str(i)+'/?key='+keyword)
        super(scrapy.Spider, self).__init__(*a, **kw)

    def parse(self, response):
        for url in self.start_urls:
            yield scrapy.http.Request(url, callback=self.parseThird)

    def parseSecond(self, response):
        item = response.meta['item']
        item['company_name'] = format(response.xpath('//a[@class="companyName"]/text()').extract()[0])
        item['salary'] = response.xpath('//span[@class="salaNum"]/strong/text()').extract()[0]
        item['job_name'] = format(response.xpath('//div[@class="xq"]/ul/li[2]/div[@class="w380"]/text()').extract()[1])
        item['location'] = response.xpath('//div[@class="xq"]/ul/li[3]/span[2]/text()').extract()[0]
        item['degree'] = format(response.xpath('//div[@class="xq"]/ul/li[1]/div[@class="fl"]/text()').extract()[1])
        item['job_year'] = format(response.xpath('//div[@class="xq"]/ul/li[2]/div[@class="fl"]/text()').extract()[1])
        item['introduction'] = format(response.xpath('//div[@id="tabC"]/div[1]/div[1]').extract()[0])
        item['character'] = format(response.xpath('//div[@class="posSumLeft"]/div[2]/ul/li[2]/text()').extract()[1])
        item['scale'] = format(response.xpath('//li[@class="scale"]/text()').extract()[1])
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