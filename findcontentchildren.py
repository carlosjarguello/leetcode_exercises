#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:55:23 2016

Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. Each child i has a greed 
factor gi, which is the minimum size of a cookie that the child will be content 
with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j 
to the child i, and the child i will be content. Your goal is to maximize the 
number of your content children and output the maximum number.

@author: carlosjarguello
"""

def findContentChildren(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        output = 0
        c1 = 0
        while c1 < len(s) and output < len(g):
            if s[c1] >= g[output]:
                output += 1
            c1 += 1
        return output