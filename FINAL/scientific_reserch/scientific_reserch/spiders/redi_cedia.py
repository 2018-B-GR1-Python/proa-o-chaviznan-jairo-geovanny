# -*- coding: utf-8 -*-
import scrapy


class RediCediaSpider(scrapy.Spider):
    name = 'redi_cedia'
    allowed_domains = ['https://redi.cedia.edu.ec/mongo/clustersTotals']
    start_urls = ['http://https://redi.cedia.edu.ec/mongo/clustersTotals/']

    def parse(self, response):
        pass
