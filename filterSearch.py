#****************************************************************
#* -*- coding: utf-8 -*-                                        *
#*  Name    : filterSeach.py                                    *
#*  Author  : Eric Araro                                        *
#*  Notice  : Copyright (c) 2021 [Banary Source]                *
#*          : All Rights Reserved                               *
#*  Date    : 12/17/2021                                        *
#*  Version : 1.0                                               *
#*  Notes   : Utiliza el archivo "searchResult.txt" con         *
#*            información de productos en mercado libre.        *
#*            Realiza una comparación de los precios            *
#*            para filtar los productos adecuados               *
#****************************************************************
import pyshorteners


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
filename = "resultSearch.txt"

# Open the file and obtain information
list_products = [[], [], [], []]
f_text = open(filename, "r")
lines_text = f_text.readlines()
i = 0
for line in lines_text:
    number, price, title, link = (item.strip() for item in line.split('] [', 3))
    number = number.replace("[","")
    price = price.replace(",", "")
    link = link.replace ("]", "")

    list_products[0].append(int(number))
    list_products[1].append(int(price))
    list_products[2].append(title)
    list_products[3].append(link)

    i += 1

# for comb in zip(list_products[0],list_products[1], list_products[2], list_products[3]):
    # print(comb[0], comb[1], comb[2], comb[3])

# Cut the URL
# shortener = pyshorteners.Shortener()
# short_url = shortener.dagd.short(list_products[3][0])
# print(short_url)

print(*[cyan, ("{:<8} {:<8} {:<30} {:<10}".format('Number', 'Price', 'Description', 'URL')), none_color])
for column in range(i):
        print("{:<8} {:<8} {:<30}".format(list_products[0][column], list_products[1][column], list_products[2][column]))

# list_products[1].sort()
# print(list_products[1])

f_text.close()
