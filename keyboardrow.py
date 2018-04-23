#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:10:49 2017

@author: carlosjarguello
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        rows = ['qwertyuiop','asdfghjkl','zxcvbnm']
        for word in words:
            for row in rows:
                if set(word.lower()).issubset(set(row)):
                    output.append(word)
        return output
                