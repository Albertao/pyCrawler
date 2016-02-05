# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    area = scrapy.Field()
    industry = scrapy.Field()
    work = scrapy.Field()
    sex = scrapy.Field()
    education = scrapy.Field()
    pass
