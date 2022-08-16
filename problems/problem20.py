# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:09:10 2022

@author: thiag
"""

# Find the sum of the digits in the number 100!

from math import factorial

N = factorial(100)

text = str(N)

value = 0
for i in text:
    value += int(i)
print(value)