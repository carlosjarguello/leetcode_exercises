#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:15:07 2016

Given an array of integers, every element appears twice except for one. 
Find that single one.

@author: carlosjarguello
"""



def singleNumber_v1(nums):  #using collections
    from collections import Counter
    temp = Counter(nums)
    for value in temp.keys():
        if  temp[value] == 1:
            return value
            
def singleNumber_v2(nums):  #using XOR
    result = 0
    for x in nums:
        result = result ^ x
    return result

            
print singleNumber_v1([1,1,2,3,3,4,4])
print singleNumber_v2([1,1,2,3,3,4,4])    
