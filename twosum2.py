#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:41:21 2017

@author: carlosjarguello
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}
        out = []
        for ind, num in enumerate(numbers):
            if num in results.keys():
                out.append(results[num]+1)
                out.append(ind+1)
                return out
            results[target - num] = ind 
