'''
-*- coding: utf-8 -*-
  Name    : filterSeach.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
  Date    : 29/12/2021
  Version : 1.1
  Notes   : Use the file productsInfo/infoMercadoLibre.json  to obtain the products
            information and filter bay price.
'''
from json import load
from os import link
import color
import pyshorteners

# Filename declaration
filename = "productsInfo/infoMercadoLibre.json"

# Parse the JSON string in the info file
with open(filename) as info_file:
    list_products = load(info_file)

# for product in range(len(list_products)):
    # print(list_products[product]['rate'])

list_final = []
for product in range(len(list_products)):
    if("price" in list_products[product]):
        list_products[product]['price'] = int( list_products[product]['price'].pop(1).replace(',', '') )

    if("rate" in list_products[product]):
        list_products[product]['rate'] = float(list_products[product]['rate'].pop(0))
        if(list_products[product]['rate'] >= 4.5):

            if("opinion_number" in list_products[product]):
                list_products[product]['opinion_number'] = int( list_products[product]['opinion_number'].pop(0).strip('Promedio entre opiniones') )
                if(list_products[product]['opinion_number'] < 10):
                    list_final.append(list_products[product])

list_final = sorted(list_final, key=lambda product : product['price'])
list_file = open("bestProduct.txt", "w")
print(*[color.cyan, ("{:<8} {:<90} {:<10}".format('Price', 'Name', 'Link')), color.reset_color])
for row in range(len(list_final)):
    link_aux = str(list_final[row]['link'])
    link_aux = link_aux.strip('[\']')
    shortener = pyshorteners.Shortener()
    short_url = shortener.dagd.short(link_aux)
    list_file.write("{:<8} {:<90} {:<10} \n".format(str(list_final[row]['price']), str(list_final[row]['name']), short_url))
    print("{:<8} {:<90} {:<10}".format(str(list_final[row]['price']), str(list_final[row]['name']), short_url))
list_file.close()
