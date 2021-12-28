'''
 -*- coding: utf-8 -*-
  Name    : mercadoLibreSpider.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
  Date    : 25/12/2021
  Version : 1.1
  Notes   : Make web Scraping on "mercadolibre.com.mx" using scrapy.
'''

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# Colors "print()"
none_color = "\033[1;00m"
black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

# Open variables file
with open("productsInfo/" + "variables.txt", "r") as f:
    lines = f.readlines()
    data_variables = {}
    i = 0
    for line in lines:
        data_variables[i] = line.strip().split('\n')
        i += 1
# Delete square brackets of the URL
page_url = str(data_variables[0])[1:-1]
search_url = str(data_variables[1])[1:-1]
page_url = page_url.replace('\'', '')
search_url = search_url.replace('\'', '')

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
        # 'CLOSESPIDER_PAGECOUNT' : 100
    }

    allowed_domains = ['articulo.mercadolibre.com.mx', 'listado.mercadolibre.com.mx']
    start_urls = [search_url]
    download_delay = 1

    rules = (
        # Pagination 
        Rule(
            LinkExtractor(
                allow=r'_Desde_\d+'
            ), follow=True),

        # Products details 
        Rule(
            LinkExtractor(
                allow=r'/MLM-'
            ), follow=True, callback='parse_items'),
    )



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

