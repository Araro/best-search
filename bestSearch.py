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
yellow = "\033[1;33m"
white = "\033[1;00m"
purple = "\033[1;35m"
# Le pregunta al usuario por la palabra clave para busqueda
search = input(yellow + "Item to search: " + purple)
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
print(driver.current_url)

# Todos los productos en una lista
products = driver.find_elements_by_xpath('//li[@class="ui-search-layout__item"]')
button = driver.find_element_by_xpath('//span[@class="andes-pagination__arrow-title"]')
count = driver.find_element_by_xpath('//li[@class="andes-pagination__page-count"]').text

# Eliminar los caracteres extras de la extracción del valor de la paginación
characters = "de "
for x in range(len(characters)):
    count = count.replace(characters[x],"")

print(yellow + count + white)
countAux = int(count)

for i in range(2):
    for product in products:
        price = product.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text
        description = product.find_element_by_xpath('.//h2[@class="ui-search-item__title"]').text

        print(price)
        print(description)

   # WebDriverWait(driver, 10).until(
   #     EC.presence_of_element_located((By.XPATH, '//span[@class="andes-pagination__arrow-title'))
   # )
   # button.click()
   # WebDriverWait(driver, 20).until(
   #     EC.presence_of_all_elements_located((By.XPATH, '//li[@class="ui-search-layout__item"]//h2[@class="ui-search-item__title"'))
   # )

driver.close()
