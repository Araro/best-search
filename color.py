'''
 !/usr/bin/env python3
 -*- coding: utf-8 -*-
  Name    : color.py
  Author  : Eric Araro
  Notice  : Copyright (c) 2021 [Banary Source]
          : All Rights Reserved
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
bblack = "\033[1;30m"
bred = "\033[1;31m"
bgreen = "\033[1;32m"
byellow = "\033[1;33m"
bblue = "\033[1;34m"
bmagenta = "\033[1;35m"
bcyan = "\033[1;36m"
bwhite = "\033[1;37m"

#Dim text
dblack = "\033[2;30m"
dred = "\033[2;31m"
dgreen = "\033[2;32m"
dyellow = "\033[2;33m"
dblue = "\033[2;34m"
dmagenta = "\033[2;35m"
dcyan = "\033[2;36m"
dwhite = "\033[2;37m"

# Italic text
iblack = "\033[3;30m"
ired = "\033[3;31m"
igreen = "\033[3;32m"
iyellow = "\033[3;33m"
iblue = "\033[3;34m"
imagenta = "\033[3;35m"
icyan = "\033[3;36m"
iwhite = "\033[3;37m"

# Text underline
ublack = "\033[4;30m"
ured = "\033[4;31m"
ugreen = "\033[4;32m"
uyellow = "\033[4;33m"
ublue = "\033[4;34m"
umagenta = "\033[4;35m"
ucyan = "\033[4;36m"
uwhite = "\033[4;37m"

# Blinking text
blblack = "\033[5;30m"
blred = "\033[5;31m"
blgreen = "\033[5;32m"
blyellow = "\033[5;33m"
blblue = "\033[5;34m"
blmagenta = "\033[5;35m"
blcyan = "\033[5;36m"
blwhite = "\033[5;37m"

# Reverses text and background colors
rblack = "\033[7;30m"
rred = "\033[7;31m"
rgreen = "\033[7;32m"
ryellow = "\033[7;33m"
rblue = "\033[7;34m"
rmagenta = "\033[7;35m"
rcyan = "\033[7;36m"
rwhite = "\033[7;37m"

# Hidden text
hblack = "\033[8;30m"
hred = "\033[8;31m"
hgreen = "\033[8;32m"
hyellow = "\033[8;33m"
hblue = "\033[8;34m"
hmagenta = "\033[8;35m"
hcyan = "\033[8;36m"
hwhite = "\033[8;37m"

# Strikethrough text
sblack = "\033[9;30m"
sred = "\033[9;31m"
sgreen = "\033[9;32m"
syellow = "\033[9;33m"
sblue = "\033[9;34m"
smagenta = "\033[9;35m"
scyan = "\033[9;36m"
swhite = "\033[9;37m"
