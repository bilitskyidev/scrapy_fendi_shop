# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapFendiPipeline(object):
	
	def __init__(self):
		self.item_list = []
    
    def process_item(self, item, spider):
        self.item_list.append(item)
    	if len(self.item_list) % 10 == 0:
    		return self.item_list
    		