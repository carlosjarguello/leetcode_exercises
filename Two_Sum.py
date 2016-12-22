#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:31:18 2016

Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

@author: carlosjarguello
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict_val = {}
    for c1 in range(len(nums)):
        if nums[c1] in dict_val.keys():
            return [dict_val[nums[c1]], c1]
        dict_val[target - nums[c1]] = c1
    return

print twoSum([2, 7, 11, 15], 9)