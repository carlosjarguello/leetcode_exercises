#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:56:09 2016

@author: carlosjarguello
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return 
    if root.left is None and root.right is None:
        return root
    temp = TreeNode(0)
    temp = root.left 
    root.left = invertTree(root.right)
    root.right = invertTree(temp)
    return root