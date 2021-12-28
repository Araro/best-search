'''
-*- coding: utf-8 -*-
  Name    : filterSeach.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
  Date    : 12/17/2021
  Version : 1.0
  Notes   : Use the file productsInfo/infoMercadoLibre.json  to obtain the products
            information and filter bay price.
'''
import pyshorteners
from json import load

# class Product:
    # def __init__(self, number, price, title, link):
        # self.number = number
        # self.price = price
        # self.title = title
        # self.link = link

# Colors for terminal "print()"
none_color = "\033[1;00m"
black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

# Filename declaration
filename = "productsInfo/infoMercadoLibre.json"

# Parse the JSON string in the info file
with open(filename) as info_file:
    list_products = load(info_file)

# print(*[red, len(list_products[0]), none_color])
# print(list_products[0]['name'])

list_price = []
for i in range(len(list_products)):
    print(list_products[i]['price'])

# Open the file and obtain information
# list_products = []
# items = [[], [], [], []]
# f_text = open(filename, "r")
# lines_text = f_text.readlines()
# i = 0
# for line in lines_text:
    # number, price, title, link = (item.strip() for item in line.split('] [', 3))
    # number = number.replace("[","")
    # price = price.replace(",", "")
    # link = link.replace ("]", "")

    # # items[0].append(int(number))
    # # items[1].append(int(price))
    # # items[2].append(title)
    # # items[3].append(link)

    # list_products.append(Product(int(number), int(price), title, link))

    # i += 1

# # Sort prices by cost
# sorted_price_low = sorted(list_products, key=lambda Product: Product.price)
# sorted_price_high = sorted(list_products, key=lambda Product: Product.price, reverse=True)

# for item in range(5):
    # # Cut the URL
    # # shortener = pyshorteners.Shortener()
    # # short_url = shortener.dagd.short(sorted_price_low[item].link)
    # print(sorted_price_low[item].price, sorted_price_low[item].title)

# for comb in zip(items[0],items[1], items[2], items[3]):
    # print(comb[0], comb[1], comb[2], comb[3])

# Dictionary of products
# dictionary_products = {}
# for pos in range(i):
    # dictionary_products[pos] = {items[0][pos]: {'Price': items[1][pos], 'Title': items[2][pos] , 'Link': items[3][pos]}}
# print(dictionary_products[0])

# print(*[cyan, ("{:<8} {:<8} {:<90} {:<50}".format('Number', 'Price', 'Description', 'URL')), none_color])
# for column in range(i):
        # print("{:<8} {:<8} {:<90}".format(items[0][column], items[1][column], items[2][column]))

# new_list = sorted(items[1])
# print(new_list)

# f_text.close()
