# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:06:04 2022

@author: thiag
"""

#What is the sum of the digits of the number 2**1000?

N = 2**1000

text = str(N)

value = 0
for i in text:
    value += int(i)
print(value)