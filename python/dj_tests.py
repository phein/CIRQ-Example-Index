#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 23:29:48 2018

@author: pyaephyohein
"""
from djsolver import djsolver
from djsolver import solve
from djsolver import random_solve

g0 = lambda x: x%2 == 0 
g1 = lambda x: 1
g2 = lambda x : x < 10

def test_g0():
    assert djsolver(g0,3) == "balanced"

def test_g1():
    assert djsolver(g1,3) == "constant"
    
def test_g2():
    assert solve(g2,3) == "constant"

def test_g3():
    assert random_solve(g0,3) == "balanced"