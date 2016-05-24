# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb as md

class MysqlPipeline(object):
    def __init__(self, dbp):
        self.dbpool = dbp


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

    @classmethod
    def from_settings(cls, settings):
        db_pool = md.connect(
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            user=settings.get('MYSQL_USER'),
            passwd=settings.get('MYSQL_PASSWORD'),
            db=settings.get('MYSQL_DB'),
            charset=settings.get('MYSQL_CHARSET')
        )
        return cls(db_pool)
