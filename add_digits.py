#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:07:40 2016

iven a non-negative integer num, repeatedly add all its digits until the 
result has only one digit.

@author: carlosjarguello
"""
def addDigits_v1(num): #Not recursive
    """
    :type num: int
    :rtype: int
    """
    #out = 0
    if num < 9:
        return num
    g = lambda x: x%10 + x/10
    out = 0
    while num > 0:
        out = g(num%10 + out)
        num = num/10
    return out
    
    
def addDigits_v2(num):    #recursive
    if num < 9:
        return num
    out = 0
    while num > 0:
        out += num%10
        num = num/10
    return addDigits_v2(out)

    
import time
t1 = time.time()
print addDigits_v1(123131231231232131)
print time.time() - t1

t1 = time.time()
print addDigits_v2(123131231231232131)
print time.time() - t1
