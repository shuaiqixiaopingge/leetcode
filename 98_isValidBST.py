# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:51:01 2019

@author: LiuZiping
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        param: root treeNode
        return: bool
        """
        if not root:
            return True
        """
        按照中序遍历算法，将二叉树转换为一数组
        判断数组是否为有序数组即可知道原二叉树是否为二叉查找树
        """
        res = self.BST2List(root)
        if len(res) == 1:
            return True
        for i in range(len(res) - 1):
            if res[i] >= res[i+1]:
                return False
        return True
    
    def BST2List(self, root):
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