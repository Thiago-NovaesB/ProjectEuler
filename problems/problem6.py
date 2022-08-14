# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:03:32 2022

@author: thiag
"""
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sum_pa(a,b=100,n=100):
    return (a+b)*n/2

def crazy_value(x=100):
    value = 0
    current_sum = sum_pa(1,x,x)
    for i in range(1,x):
        current_sum -= i
        value += i*current_sum
    return 2*value