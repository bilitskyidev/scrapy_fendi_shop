# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from fendi.tasks import add_scrap_item
from scrapy.signals import spider_closed


class ScrapFendiPipeline(object):
    item_list = []


    def process_item(self, item, spider):
        self.item_list.append(item)
        if len(self.item_list) == 10:
            add_scrap_item(self.item_list)
            self.item_list = []
        return item

    def spider_closed(self, spider, reason):
        add_scrap_item(self.item_list, end=True)
        return 'Finish scraping'
