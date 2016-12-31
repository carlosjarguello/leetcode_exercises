#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:22:32 2016

You are playing the following Nim Game with your friend: There is a heap of 
stones on the table, each time one of you take turns to remove 1 to 3 stones. 
The one who removes the last stone will be the winner. You will take the 
first turn to remove the stones.

@author: carlosjarguello
"""
def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    return n%4 != 0

    
print canWinNim(5)