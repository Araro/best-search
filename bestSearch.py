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
# print(f"El producto a buscar es: {search}")

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

# Accept cockies
try:
    buttonCockies = driver.find_element_by_id("newCookieDisclaimerButton")
    buttonCockies.click()
except Exception as e:
    print(red)
    print(e)
    print(white)

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

## Product list of the page
products = driver.find_elements_by_class_name("ui-search-result__wrapper")
for product in products:
    itemPrice = product.find_element_by_class_name("price-tag-fraction").text
    itemTitle = product.find_element_by_tag_name("h2").text
    itemLink = product.find_element_by_tag_name('a').get_attribute('href')

    print(itemPrice)
    print(itemTitle)
    print(itemLink)

# Obtaining information about the products of the search
i = 1
while(i < countAux):
    ## Pagination button
    try:
        buttonNext = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        buttonNext.click()
    except Exception as e:
        print(red)
        print(e)
        print(white)
        break

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

    ## Product list of the page
    products = driver.find_elements_by_class_name("ui-search-result__wrapper")
    for product in products:
        itemPrice = product.find_element_by_class_name("price-tag-fraction").text
        itemTitle = product.find_element_by_tag_name("h2").text
        itemLink = product.find_element_by_tag_name('a').get_attribute('href')


        print(itemPrice)
        print(itemTitle)
        print(itemLink)

    i += 1

driver.close()
