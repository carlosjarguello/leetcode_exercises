#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:34:02 2016

Calculate the sum of two integers a and b, but you are not allowed to 
use the operator + and -.

@author: carlosjarguello
"""

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    carry = 0
    while (b != 0): 
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
    
def getSubtract(a, b):
    borrow = 0 	
    while (b != 0): 
        borrow = (~a) & b;
        a = a ^ b;
        b = borrow << 1;
	return a
    
def getSum_v2(a, b): #Not my solution, fixes python integer issues
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
 
print getSum(11,-1)
    
