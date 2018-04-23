#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:01:53 2017

@author: carlosjarguello
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_zeros = 0
        curr_zeros = 0
        for x in nums:
            if x == 1:
                curr_zeros += 1
            else:
                if max_zeros < curr_zeros:
                    max_zeros = curr_zeros
                curr_zeros = 0
        if max_zeros < curr_zeros:
            max_zeros = curr_zeros
        return max_zeros