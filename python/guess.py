# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

num = random.randint(1,11)

g = lambda x: x%2 == 0 

#f(num)
def djsolver (f,n):
    print(n)
    for c in range(1,(2**(n-1)+1)):
        print (c)
        print (f(c))
        if f(c) != f(0): 
            return ("balanced")

    return ("constant")

print(djsolver(g,3))
