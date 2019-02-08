import scrapy
from scrapy.loader import ItemLoader

from UsedCarResearch.utils import info_cleaners
from UsedCarResearch.properties import data_properties
from UsedCarResearch.items import OlxUsedCar

path_file = 'data.csv'


class OlxSpider(scrapy.Spider):
    name = 'olx_spider'

    def start_requests(self):
        urls = [
            'https://quito.olx.com.ec/coches-cat-378'
        ]
        for page in range(2, 304):
            urls.append('https://quito.olx.com.ec/coches-cat-378-p-{}'.format(page))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        search = response.css('ul.items-list > li.item')

        for item in search:
            item_info = item.css('div > div.items-info > h3 > a::text').extract_first()
            item_location = item.css('div > div.items-info > span.displayLocation::text').extract_first()
            item_price = item.css('div > p.items-price > a::text').extract_first()
            item_price_negotiation = item.css('div > p.items-price > a > span.price-type::text').extract_first()
            item_date_published = item.css('div > p.items-date::text').extract_first()

            with open(path_file, 'a+') as file:
                line = '{};{};{};{};{}\n'.format(
                    info_cleaners.clean_only_text(item_info),
                    info_cleaners.clean_only_text(item_location),
                    info_cleaners.clean_only_text(item_price, with_space=False, data_type=data_properties.TEXT),
                    info_cleaners.clean_only_text(item_price_negotiation),
                    info_cleaners.clean_only_text(item_date_published, with_space=False,
                                                  data_type=data_properties.TEXT)
                )
                file.write(line)



