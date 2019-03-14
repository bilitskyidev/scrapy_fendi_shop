# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapFendiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    description = scrapy.Field()
    color = scrapy.Field()
