# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    company_name = scrapy.Field()
    salary = scrapy.Field()
    degree = scrapy.Field()
    job_name = scrapy.Field()
    location = scrapy.Field()
    job_year = scrapy.Field()
    introduction = scrapy.Field()
