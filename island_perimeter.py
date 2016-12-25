#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:01:33 2016

@author: carlosjarguello
"""

def islandPerimeter(grid): #My naive solution, not the best, but works 
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for x in range(rows):
        grid[x] = [0] + grid[x] + [0]
    grid.append([0 for _ in range(cols+2)])
    grid = [[0 for _ in range(cols+2)]] + grid
    for c1 in range(rows):
        for c2 in range(cols):
            if grid[c1+1][c2+1] == 1:
                for c3 in [-1,1]:
                    if grid[c1+1+c3][c2+1] == 0:
                        perimeter += 1
                for c4 in [-1,1]:
                    if grid[c1+1][c2+1+c4] == 0:
                        perimeter += 1
    return perimeter

def islandPerimeter_v2(grid): #Not my solution, but it is a smart one
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    h = len(grid)
    w = len(grid[0]) if h else 0
    ans = 0
    for x in range(h):
        for y in range(w):
            if grid[x][y] == 1:
                ans += 4
                if x > 0 and grid[x - 1][y]:
                    ans -= 2
                if y > 0 and grid[x][y - 1]:
                    ans -= 2
    return ans

print islandPerimeter([[0,0,0,0],[0,1,1,0],[0,0,0,0]])