#****************************************************************
#* -*- coding: utf-8 -*-                                        *
#*  Name    : bestSeach.py                                      *
#*  Author  : Eric Araro                                        *
#*  Notice  : Copyright (c) 2021 [Banary Source]                *
#*          : All Rights Reserved                               *
#*  Date    : 12/11/2021                                        *
#*  Version : 1.0                                               *
#*  Notes   : Utiliza la librería "Selenium" para obtener       *
#*            información de productos en mercado libre.        *
#*            Además de hacer una comparación de los precios    *
#*            para filtar los productos adecuados               *
#****************************************************************

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm

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

# Ask to the user the search key words
search = input(yellow + "Item to search: " + magenta)
print(white)

# Declaration of Driver (Chrome)
driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get("http://www.mercadolibre.com.mx")
print(yellow + driver.title + white)
assert "Mercado" in driver.title
elem = driver.find_element(By.NAME, "as_word")
elem.clear()
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(yellow + driver.current_url + white)

# Create file to save information of the search
f = open('resultSearch.txt','w')

# Number of pages of the search
count = driver.find_element(By.XPATH, '//li[@class="andes-pagination__page-count"]').text
## Eliminar los caracteres extras de la extracción del valor de la paginación
characters = "de "
for x in range(len(characters)):
    count = count.replace(characters[x],"")

print(yellow + "Number of pages: " + cyan + count + white)
count_aux = int(count)

# Accept cockies
try:
    button_cockies = driver.find_element(By.ID, "newCookieDisclaimerButton")
    button_cockies.click()
except Exception as e:
    print(*[red, e, white])

# Obtaining information about the products of the search
print(green, "Obtainig information...", none_color)
i = 0
n = 1
## "tqdm" is the progress bar
for i in tqdm(range(count_aux)):
    # Urls of Items
    ## pageAux and pageType helps distinguish between the two different types of pages
    try:
        page_aux=driver.find_element(By.XPATH, '//h2[@class="ui-search-item__title"]')
        page_aux=True
        page_type=True
    except:
        page_aux = False
        page_type = False

    ## Product charlist of the page
    products = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")
    for product in products:
        item_price = product.find_element(By.CLASS_NAME, "price-tag-fraction").text
        item_title = product.find_element(By.TAG_NAME, "h2").text
        item_link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')

        n_aux = str(n)
        data = "[%s] [%s] [%s] [%s]\n"%(n_aux, item_price, item_title, item_link)
        f.write(data)

        n += 1

    ## Pagination button
    if(i<(count_aux-1)):
        try:
            button_next = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
            button_next.click()
        except Exception as e:
            print(*[red, e, white])
            break

    i += 1
f.close()
driver.close()
