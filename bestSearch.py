'''
 -*- coding: utf-8 -*-
  Name    : bestSeach.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
  Date    : 24/12/2021
  Version : 1.1
  Notes   : Obtain the search URL from "mercadolibre.com.mx" using Selenium.
            Send de information to the scrapy file.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import sys
import os

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
# search = input(yellow + "Item to search: " + magenta)
# print(white)

# chrome_options = Options()
# chrome_options.add_argument(
    # "USER_AGENT = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
# )
# platform = "http://www.mercadolibre.com.mx"
#*******************************************************************
# Functions definitions
#*******************************************************************
def init_search_chrome(product_to_search):
    # Declaration of Driver (Chrome)
    chrome_options = Options()
    chrome_options.add_argument("USER_AGENT = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
    page_url = "http://www.mercadolibre.com.mx"
    driver = webdriver.Chrome(service=Service('./chromedriver'), options=chrome_options)
    driver.get(page_url)
    print(yellow + driver.title + none_color)
    assert "Mercado" in driver.title
    elem = driver.find_element(By.NAME, "as_word")
    elem.clear()
    elem.send_keys(product_to_search)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    search_url = driver.current_url
    driver.close()
    # Save page_url and search_url in a file
    with open("productsInfo/" + "variables.txt", "w") as f:
        f.write(page_url + "\n")
        f.write(search_url)
    return (page_url, search_url)

def standalone_search(product_to_search):
    print(cyan + product_to_search + none_color)
    init_search_chrome(product_to_search)
    os.system("scrapy runspider mercadoLibreSpider.py --overwrite-output=productsInfo/infoMercadoLibre.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {:s} <Product to search>".format(sys.argv[0]))
        print("example: py bestsearch.py 'audifonos skullcandy'".format(sys.argv[0]))
        sys.exit(1)

    standalone_search(sys.argv[1])

# # Create file to save information of the search
# f = open('resultSearch.txt','w')

# # Number of pages of the search
# count = driver.find_element(By.XPATH, '//li[@class="andes-pagination__page-count"]').text
# ## Eliminar los caracteres extras de la extracción del valor de la paginación
# characters = "de "
# for x in range(len(characters)):
    # count = count.replace(characters[x],"")

# print(yellow + "Number of pages: " + cyan + count + white)
# count_aux = int(count)

# # Accept cockies
# try:
    # button_cockies = driver.find_element(By.ID, "newCookieDisclaimerButton")
    # button_cockies.click()
# except Exception as e:
    # print(*[red, e, white])

# # Obtaining information about the products of the search
# print(green, "Obtainig information...", none_color)
# i = 0
# n = 1
# ## "tqdm" is the progress bar
# for i in tqdm(range(count_aux)):
    # # Urls of Items
    # ## pageAux and pageType helps distinguish between the two different types of pages
    # try:
        # page_aux=driver.find_element(By.XPATH, '//h2[@class="ui-search-item__title"]')
        # page_aux=True
        # page_type=True
    # except:
        # page_aux = False
        # page_type = False

    # ## Product charlist of the page
    # products = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")
    # for product in products:
        # item_price = product.find_element(By.CLASS_NAME, "price-tag-fraction").text
        # item_title = product.find_element(By.TAG_NAME, "h2").text
        # item_link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # n_aux = str(n)
        # data = "[%s] [%s] [%s] [%s]\n"%(n_aux, item_price, item_title, item_link)
        # f.write(data)

        # n += 1

    # ## Pagination button
    # if(i<(count_aux-1)):
        # try:
            # button_next = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
            # button_next.click()
        # except Exception as e:
            # print(*[red, e, white])
            # break

    # i += 1
# f.close()
# driver.close()
