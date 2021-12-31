'''
 -*- coding: utf-8 -*-
  Name    : mercadoLibreSpider.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
  Date    : 12/25/2021
  Version : 1.1
  Notes   : Make web Scraping on "mercadolibre.com.mx" using scrapy.
'''

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from scrapy import Request
import color

# Open variables file
with open("productsInfo/" + "urlMercadoLibre.txt", "r") as f:
    lines = f.readlines()
    url_products = {}
    i = 0
    for line in lines:
        url_products[i] = line.strip().lstrip('[').rstrip(']')
        i += 1

print(len(url_products))
#*******************************************************************
# Class definitions
#*******************************************************************
class Product(Item):
    name = Field()
    price = Field()
    description = Field()
    discount_percent = Field()
    rate = Field()
    opinion_number = Field()
    sale = Field()
    stock = Field()
    link = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
    }

    download_delay = 1
    allowed_domains = ['articulo.mercadolibre.com.mx', 'listado.mercadolibre.com.mx']

    def start_requests(self):
        for url in range(len(url_products)):
            yield Request(url_products[url], self.parse_items)

    def parse_items(self, response):
        item = ItemLoader(Product(), response)

        item.add_xpath('name',
                        '//h1/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )
        item.add_xpath('price',
                        '//div[@class="ui-pdp-price__second-line"]/span/span/span/text()',
                        MapCompose(lambda i: i.replace('\n', '  ').replace('\r', '  ').strip())
                        )

        item.add_xpath('description',
                        '//div[@class="ui-pdp-description"]/p/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )

        item.add_xpath('discount_percent',
                        '//span[@class="ui-pdp-price__second-line__label ui-pdp-color--GREEN ui-pdp-size--MEDIUM"]/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )

        item.add_xpath('rate',
                        '//p[@class="ui-pdp-reviews__rating__summary__average"]/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )

        item.add_xpath('opinion_number',
                        '//p[@class="ui-pdp-reviews__rating__summary__label"]/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )

        item.add_xpath('sale',
                        '//span[@class="ui-pdp-subtitle"]/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )

        item.add_xpath('stock',
                        '//span[@class="ui-pdp-buybox__quantity__available"]/text()',
                        MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip())
                        )

        actual_url = response.url
        item.add_value('link', actual_url)

        yield item.load_item()

#*****************  End Class definitions  *************************
#*******************************************************************

