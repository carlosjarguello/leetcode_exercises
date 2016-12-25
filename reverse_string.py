#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 12:41:11 2016

Write a function that takes a string as input and returns the string reversed.

@author: carlosjarguello
"""

def reverseString(s):
    #list_temp = list(s)
    out_list = []
    #while(list_temp):
        #out_list.append(list_temp.pop())
    #return "".join(out_list)
    for x in range(len(s)):
        out_list.append(s[len(s)-x-1])    
    return "".join(out_list)

print reverseString('hello')
        
        