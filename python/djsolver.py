# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np

num = random.randint(1,11)

g0 = lambda x: x%2 == 0 
g1 = lambda x: 1
g2 = lambda x : x < 10

def get_list():
    a = []
    for i in range(11):
        a = a.append(num)
    return a
#print(get_list())  

l0 = [2, 5, 10, 6, 8, 14, 12, 9]



def solve(f,n):
    val = np.random.permutation((2**n)-1)
    for i in range((n//4)+1):
        #print(i)
        print(int(f(i)))
        print(int(f((len(val) -1) -i)))
        if f(i) != f((len(val) -1) -i):
            return ("balanced")
    return ("constant")
#print(solve(g0,4))
#print(solve(g1,4))

def djsolver (f,n):
    for c in range(1,(2**(n-1)+1)):
        print (c)
        print (f(c))
        if f(c) != f(0): 
            return ("balanced")

    return ("constant")

#print(djsolver(g0,3))
#print(djsolver(g1,5))
    
def random_solve(f,n):
    a = b = 0
    while a == b:
        val = np.random.randint(0,high=(2**n),size=(2,1))
        print(val)
        a = val[0]
        b = val[1]
        
    
    print(a)
    print(b)
    if f(a) != f(b):
        return("balanced")
    else :
        return np.random.choice(["balanced","constant"],p=[1/3,2/3])
        
#print(random_solve(g0,4))
        
def Nrandom_solve(f,n,k):
    count =  0
    for i in range(k):
        random_solve(f,n)
        if random_solve(f,n) == "balanced":
            count = count + 1
    if count > (k-count):
        return ("balanced")
    else:
        return ("constant")
        

#print(Nrandom_solve(g0,3,5))

    