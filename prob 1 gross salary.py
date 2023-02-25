# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:03:34 2023

@author: gowtham reddy
"""

def sac(x,a,b,c,t):
    return t*(x-((a+b+c)/100)*x)
x=int(input()) #gross salary
a=float(input())#federal deduction
b=float(input())#state deduction
c=float(input())#company's pension plan
t=int(input())#no. of weeks
print(sac(x,a,b,c,t))

    