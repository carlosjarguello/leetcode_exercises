#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:35:49 2016
The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.
@author: carlosjarguello
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right)+1
        if root.right is None:
            return self.minDepth(root.left) +1
        left_d = 1 + self.minDepth(root.left)
        right_d = 1 + self.minDepth(root.right)
        if left_d < right_d:
            return left_d
        else:
            return right_d

