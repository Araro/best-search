'''
 -*- coding: utf-8 -*-
  Name    : bestSeach.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
  Date    : 12/24/2021
  Version : 1.1
  Notes   : Obtain the search URL from "mercadolibre.com.mx" using Selenium.
            Send de information to the scrapy file.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import sys
import color
import os


#***********      Search the product's URLs and save the information in a file.txt          *********#   
#****************************************************************************************************#
def get_product_url(driver):
    # # Create file to save information of the search
    f = open("productsInfo/" + "urlMercadoLibre.txt", "w")
    # Number of pages of the search
    number_of_pages = driver.find_element(By.XPATH, '//li[@class="andes-pagination__page-count"]').text
    ## Eliminar los caracteres extras de la extracción del valor de la paginación
    characters = "de "
    for x in range(len(characters)):
        number_of_pages = number_of_pages.replace(characters[x],"")

    print(color.yellow + "Number of pages: " + color.cyan + number_of_pages + color.reset_color)
    count_aux = int(number_of_pages)

    # Accept cockies
    try:
        button_cockies = driver.find_element(By.ID, "newCookieDisclaimerButton")
        button_cockies.click()
    except Exception as e:
        print(*[color.red, e, color.reset_color])

    # Obtaining information about the products of the search
    print(color.green, "Obtainig information...", color.reset_color)
    i = 0
    n = 0
    ## "tqdm" is the progress bar
    # for i in tqdm(range(count_aux)):
    for i in tqdm(range(3)):
        # Urls of Items
        ## Wait until the page is loaded
        delay = 3 # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        except TimeoutException:
            print("Loading took too much time!")

        ## Distinguish between the two different types of pages
        try:
            driver.find_element(By.XPATH, '//h2[@class="ui-search-item__title"]')
        except:
            pass

        ## Product charlist of the page
        products = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")
        for product in products:
            item_link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')

            data = "[%s]\n"%(item_link)
            f.write(data)

            n += 1

        ## Pagination button
        if(i<(count_aux-1)):
            try:
                button_next = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
                button_next.click()
            except Exception as e:
                print(*[color.red, e, color.reset_color])
                break

        i += 1
    print(color.blue + "Number of products: " + color.ired + str(n) + color.reset_color)
    f.close()
    driver.close()

#*********            Inicialize Chrome web driver with the key search             *************#
#***********************************************************************************************#
def init_search_chrome(product_to_search):
    # Declaration of Driver (Chrome)
    chrome_options = Options()
    chrome_options.add_argument("USER_AGENT = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
    page_url = "http://www.mercadolibre.com.mx"
    driver = webdriver.Chrome(service=Service('./chromedriver'), options=chrome_options)
    driver.get(page_url)
    print(color.yellow + driver.title + color.reset_color)
    assert "Mercado" in driver.title
    elem = driver.find_element(By.NAME, "as_word")
    elem.clear()
    elem.send_keys(product_to_search)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    search_url = driver.current_url

    # Save page_url and search_url in a file
    with open("productsInfo/" + "variables.json", "w") as f:
        f.write(page_url + "\n")
        f.write(search_url)
    get_product_url(driver)

def standalone_search(product_to_search):
    print(color.cyan + product_to_search + color.reset_color)
    init_search_chrome(product_to_search)
    # os.system("scrapy runspider mercadoLibreSpider.py --overwrite-output=productsInfo/infoMercadoLibre.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {:s} <Product to search>".format(sys.argv[0]))
        print("example: py bestsearch.py 'audifonos skullcandy'".format(sys.argv[0]))
        sys.exit(1)

    standalone_search(sys.argv[1])
