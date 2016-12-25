#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:10:48 2016

The Hamming distance between two integers is the number of positions at 
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

@author: carlosjarguello
"""

def hammingDistance(x, y):
    output = 0
    while (x > 0 or y > 0):
        output += abs(x%2 - y%2)
        x/=2
        y/=2
    return output
    
print hammingDistance(7,0)
    
    