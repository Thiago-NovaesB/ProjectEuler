# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:36:15 2022

@author: thiag
"""
# Find the sum of all the primes below two million

N = 2000000
primes = list(range(2,N+1))

for i in range(N-1):
    if primes[i] != 0:
        for j in range(primes[i],N+1):
            if primes[i]*j <= N:
                primes[primes[i]*j - 2] = 0
            else:
                break
print(sum(primes))
            