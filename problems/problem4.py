# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:34:52 2022

@author: thiag
"""
#Find the largest palindrome made from the product of two 3-digit numbers.
def update_c(c,current_max):
    text = str(c)
    if text[::-1] == text:
        return max(c,current_max)
    else:
        return current_max

def update_ab(a,b):
    if b != 1:
        return a, b-1
    else:
        return a-1, a-1

def check_last(c):
    return c != 1

a = 999
b = 1000

current_max = 0

check = True

while check:
    a, b = update_ab(a,b)
    c = a*b
    current_max = update_c(c,current_max)
    check = check_last(c)
    
print(a,b)
    
        