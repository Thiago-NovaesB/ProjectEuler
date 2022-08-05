# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:46:15 2022

@author: thiag
"""
def an(x, r):
    if x%r == 0:
        return x - r
    else:
        return x - (x%r)

def Sn(x, r):
    sup = an(x, r)
    n = (sup - r)/r + 1
    return n*(r+sup)/2


assert(Sn(10,3) + Sn(10,5) - Sn(10,15) == 23)

print(int(Sn(1000,3) + Sn(1000,5) - Sn(1000,15)))