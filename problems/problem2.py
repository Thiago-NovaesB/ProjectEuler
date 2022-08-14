# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:46:15 2022

@author: thiag
"""
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def sum_even_fib():
	x = y = 1
	sum = 0
	while (sum < 1000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum