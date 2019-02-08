# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxUsedCar(scrapy.Item):
    info = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    negotiation = scrapy.Field()
    date_published = scrapy.Field()
