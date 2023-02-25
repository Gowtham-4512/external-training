# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:31:18 2023

@author: gowtham reddy
"""
import time
#using slicing
def reverseusingslicing(s):
    return s[::-1]

#using recusion
def reverseusingrecursion(s):
    n=len(s)
    if n==0:
        return ""
    return s[-1]+reverseusingrecursion(s[0:n-1])

a=input()
x=time.time()
l=reverseusingslicing(a)
print(l)
y=time.time()
print("using slicing",y-x)
"""
c=time.time()
b=reverseusingrecursion(a)
print(b)
d=time.time()
print("using recursion",d-c)
"""