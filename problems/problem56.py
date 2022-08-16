# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:17:53 2022

@author: thiag
"""

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

maximum = 0

for a in range(1,101):
    for b in range(1,101):
        value = a**b
        text = str(value)
        current = 0
        for i in text:
            current += int(i)
        maximum = max(current,maximum)
        
print(maximum)