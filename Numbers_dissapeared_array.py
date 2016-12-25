#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 12:38:49 2016
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.
@author: carlosjarguello
"""

def findDisappearedNumbers(nums):
    #return list(set(range(1,len(nums)+1)) - set(nums)) works but too slow!
    out = []
    temp = [0]*(len(nums))
    for x in nums:
        temp[x-1] = 1
    for c1,x in enumerate(temp):
        if x == 0:
            out.append(c1+1)
    return out
    
print findDisappearedNumbers([4,3,2,7,8,2,3,1])