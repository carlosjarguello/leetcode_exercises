#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:41:32 2016

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and 
for the multiples of five output “Buzz”. For numbers which are multiples of 
both three and five output “FizzBuzz”.

@author: carlosjarguello
"""

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = []
    for x in range(1,n+1):
        if x%15 == 0:
            output.append('FizzBuzz')
        elif x%3 == 0:
            output.append('Fizz')
        elif x%5 == 0:
            output.append('Buzz')
        else:
            output.append(str(x))
    return output
    
out = fizzBuzz(15)
print out
        
            