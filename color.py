'''
 !/usr/bin/env python3
 -*- coding: utf-8 -*-
  Name    : color.py
  Author  : Eric Araro
  Notice  : MIT Licence
  Date    : 12/28/2021
  Version : 1.0
  Notes   : Colors and styles to use in ubuntu prompt, print().
'''

# Colors "print()"
reset_color = "\033[0;00m"
bold = "\033[1;00m"
dim = "\033[2;00m"
italic = "\033[3;00m"
underline = "\033[4;00m"
blink = "\033[5;00m"
reverse = "\033[7;00m"
hidden = "\033[8;00m"
Strikethrough = "\033[9;00m"

# Normal text 
## Normal text (This is the default value even if no attribute is set)
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

# Bold text
## In the Ubuntu Terminal, this value specifies bold text
blackb = "\033[1;30m"
redb = "\033[1;31m"
greenb = "\033[1;32m"
yellowb = "\033[1;33m"
blueb = "\033[1;34m"
magentab = "\033[1;35m"
cyanb = "\033[1;36m"
whiteb = "\033[1;37m"

#Dim text
blackd = "\033[2;30m"
redd = "\033[2;31m"
greend = "\033[2;32m"
yellowd = "\033[2;33m"
blued = "\033[2;34m"
magentad = "\033[2;35m"
cyand = "\033[2;36m"
whited = "\033[2;37m"

# Italic text
blacki = "\033[3;30m"
redi = "\033[3;31m"
greeni = "\033[3;32m"
yellowi = "\033[3;33m"
bluei = "\033[3;34m"
magentai = "\033[3;35m"
cyani = "\033[3;36m"
whitei = "\033[3;37m"

# Text underline
blacku = "\033[4;30m"
redu = "\033[4;31m"
greenu = "\033[4;32m"
yellowu = "\033[4;33m"
blueu = "\033[4;34m"
magentau = "\033[4;35m"
cyanu = "\033[4;36m"
whiteu = "\033[4;37m"

# Blinking text
blackbl = "\033[5;30m"
redbl = "\033[5;31m"
greenbl = "\033[5;32m"
yellowbl = "\033[5;33m"
bluebl = "\033[5;34m"
magentabl = "\033[5;35m"
cyanbl = "\033[5;36m"
whitebl = "\033[5;37m"

# Reverses text and background colors
blackr = "\033[7;30m"
redr = "\033[7;31m"
greenr = "\033[7;32m"
yellowr = "\033[7;33m"
bluer = "\033[7;34m"
magentar = "\033[7;35m"
cyanr = "\033[7;36m"
whiter = "\033[7;37m"

# Hidden text
blackh = "\033[8;30m"
redh = "\033[8;31m"
greenh = "\033[8;32m"
yellowh = "\033[8;33m"
blueh = "\033[8;34m"
magentah = "\033[8;35m"
cyanh = "\033[8;36m"
whiteh = "\033[8;37m"

# Strikethrough text
blacks = "\033[9;30m"
reds = "\033[9;31m"
greens = "\033[9;32m"
yellows = "\033[9;33m"
blues = "\033[9;34m"
magentas = "\033[9;35m"
cyans = "\033[9;36m"
whites = "\033[9;37m"
