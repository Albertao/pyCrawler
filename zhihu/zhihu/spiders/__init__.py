# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class zhihuSpider(scrapy.Spider):
    name = "users"

    start_urls = ['http://www.zhihu.com/people/tan-quan-lin']

    def parse(self, response):
        filename = "test.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
