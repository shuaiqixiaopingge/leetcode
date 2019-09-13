# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:19:00 2019

@author: LiuZiping
"""
class treeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def binaryTreeInorderTraversal(root):
    """
    param:treeNode root
    return: List[int]
    """
    if not root:
        return None
    stack = []
    res = []
    t = root
    while t:
        stack.append(t)
        t = t.left
    while stack:
        item = stack.pop()
        res.append(item.val)
        t = item.right
        while t:
            stack.append(t)
            t = t.left
    return res