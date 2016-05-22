# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb as md
from scrapy.conf import settings

class MysqlPipeline(object):
    def __init__(self):
        self.dbpool = md.connect(
            host="localhost",#settings['MYSQL_HOST'],
            port=3306,#settings['MYSQL_PORT'],
            user="root",#settings['MYSQL_USER'],
            passwd="hsb4325HSB",#settings['MYSQL_PASSWORD'],
            db="crawl",#settings['MYSQL_DB'],
            charset="utf8"
        )


    def process_item(self, item, spider):
        cur = self.dbpool.cursor()
        cur.execute(\
                "insert into jobs (`id`, `url`, `company_name`, `salary`, `degree`, `job_name`, `location`, `job_year`, `introduction`)\
                values (null, %s, %s, %s, %s, %s, %s, %s, %s)",

                (item['url'],
                 item['company_name'],
                 item['salary'],
                 item['degree'],
                 item['job_name'],
                 item['location'],
                 item['job_year'],
                 item['introduction'])
                )
        self.dbpool.commit()