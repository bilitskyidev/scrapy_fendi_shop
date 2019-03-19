# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from fendi.tasks import add_scrap_item
from scrapy import signals


class ScrapFendiPipeline(object):
    item_list = []

    def process_item(self, item, spider):
        self.item_list.append(dict(item))
        if len(self.item_list) == 20:
            add_scrap_item.delay(self.item_list)
            self.item_list = []
        return item

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_idle,
                                signal=signals.spider_idle)
        return pipeline

    def spider_idle(self):
        if len(self.item_list) > 0:
            add_scrap_item.delay(self.item_list, end=True)
            print('Sending last {} items'.format(len(self.item_list)))
            self.item_list = []
