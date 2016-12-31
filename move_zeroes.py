#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:18:15 2016

@author: carlosjarguello
"""

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    c1 = 0
    c2 = 0
    while c2 < len(nums):
        if nums[c1] == 0:
            for c3 in range(c1,len(nums)-1):
                nums[c3] = nums[c3+1]
            nums[len(nums)-1] = 0
        else:
            c1+=1
        c2 +=1
    return nums

print moveZeroes([0,1,0,0,123,0,2,0,0,2,2,0])