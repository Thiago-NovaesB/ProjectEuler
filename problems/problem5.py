# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:20:24 2022

@author: thiag
"""
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto

    return a

value = 1

for i in range(2,21):
    value *= i / mdc(value,i)
    
print(value)