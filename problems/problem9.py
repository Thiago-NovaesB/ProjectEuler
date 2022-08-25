# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:42:42 2022

@author: thiag
"""
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

def brute_force():
    for a in range(1,500):
        for b in range(1,500):
            for c in range(1,500):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    return a*b*c
                