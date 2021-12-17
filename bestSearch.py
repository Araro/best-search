#****************************************************************
#* -*- coding: utf-8 -*-                                        *
#*  Name    : bestSeach.py                                      *
#*  Author  : Eric Araro                                        *
#*  Notice  : Copyright (c) 2021 [Banary Source]                *
#*          : All Rights Reserved                               *
#*  Date    : 12/11/2021                                        *
#*  Version : 1.0                                               *
#*  Notes   : Utiliza la librería "Scrapy" para obtener         *
#*            información de productos en mercado libre.        *
#*            Además de hacer una comparación de los precios    *
#*            para filtar los productos adecuados               *
#****************************************************************

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Declraración de colores para utilizar en "print()"
black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
# Le pregunta al usuario por la palabra clave para busqueda
search = input(yellow + "Item to search: " + magenta)
print(white)
# print(f"El producto a buscar es: {producto}")

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.mercadolibre.com.mx")
print(yellow + driver.title + white)
assert "Mercado" in driver.title
elem = driver.find_element_by_name("as_word")
elem.clear()
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(yellow + driver.current_url + white)


# Number of pages of the search
count = driver.find_element_by_xpath('//li[@class="andes-pagination__page-count"]').text
## Eliminar los caracteres extras de la extracción del valor de la paginación
characters = "de "
for x in range(len(characters)):
    count = count.replace(characters[x],"")

print(yellow + "Number of pages: " + cyan + count + white)
countAux = int(count)

# Urls of Items
## pageAux and pageType helps distinguish between the two different types of pages
try:
    pageAux=driver.find_element_by_xpath('//h2[@class="ui-search-item__title"]')
    pageAux=True
    pageType=True
    print(cyan + "1st option" + white)
except:
    pageAux = False
    pageType = False
    print(cyan + "2nd option" + white)

# Links of the products and product list of the page
if(pageAux==True):
    link_products = driver.find_elements_by_xpath('//a[@class="ui-search-item__group__element ui-search-link"]')
    # products = driver.find_elements_by_xpath('//li[@class="ui-search-layout__item"]')
    products = driver.find_elements_by_class_name("ui-search-result__wrapper")
else:
    link_products = driver.find_elements_by_xpath('//a[@class="ui-search-result__content ui-search-link"]')
    products = driver.find_elements_by_class_name("ui-search-result__wrapper")

links_page = []
for tag_a in link_products:
    links_page.append(tag_a.get_attribute("href"))

# for link in links_page:
    # try:
        # driver.get(link)
        # Item_name = driver.find_element_by_xpath('//h1').text
        # Item_price = driver.find_element_by_xpath('//span[@class="price-tag-fraction"]').text
        # print(Item_name)
        # print(Item_price)
        # driver.back()
    # except Exception as e:
        # print(red)
        # print(e)
        # print(white)
        # driver.back()

for product in products:
    if(pageType ==  True):
        # itemPrice = product.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text
        # itemTitle = product.find_element_by_xpath('.//h2[@class="ui-search-item__title"]').text
        itemPrice = product.find_element_by_class_name("price-tag-fraction").text
        itemTitle = product.find_element_by_tag_name("h2").text


        print(itemPrice)
        print(itemTitle)
    else:
        itemPrice = product.find_element_by_class_name("price-tag-fraction").text
        itemTitle = product.find_element_by_tag_name("h2").text

        print(itemPrice)
        print(itemTitle)

driver.close()
