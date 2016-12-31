#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:18:15 2016

@author: carlosjarguello
"""

def moveZeroes_dumb(nums):
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

def moveZeroes_smart(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    slow_ptr = 0
    for fast_ptr in range(len(nums)):
        if nums[fast_ptr]:
            nums[fast_ptr], nums[slow_ptr] = nums[slow_ptr], nums[fast_ptr]
            slow_ptr += 1
    return nums
    
import time
import random
a = range(10000)
for _ in range(30):
    a[random.randint(0,10000)] = 0
t1 = time.time()
moveZeroes_dumb(a)
print time.time() - t1
t1 = time.time()
moveZeroes_smart(a)
print time.time() - t1