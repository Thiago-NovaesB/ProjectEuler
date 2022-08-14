# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:30:05 2022

@author: thiag
"""

#What is the largest prime factor of the number 600851475143 ?

def divide(x, n):
    if x % n == 0:
        return x / n
    else:
        return x
x = 600851475143

n = 1
while x != 1:
    n += 1
    x = divide(x, n)

print(n)