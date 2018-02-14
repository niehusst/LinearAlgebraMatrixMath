#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sympy import solve, evalf
#from Matrix import *
"""
Created on Mon Feb 12 23:41:14 2018

@author: Liam2
"""
#y = Symbol('y')
x = str(2*y**2 + 4*y - 1)
lst = solve(x, y)
def setter(l):
    for i in range(len(l)):
        l[i] = l[i].evalf()
    return l
lst = setter(lst)
print(lst)
#m = Matrix(2,2)
