# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:42:59 2019

@author: LiuZiping
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        param: treeNode root
        return: List[int]
        """
        """
        与层序遍历几乎一样
        只需加入一个flag来判断时正向出栈还是反向出栈
        """
        if not root:
            return None
        flag = False
        stack = [root, None]
        res = []
        levelNode = []
        while stack:
            t = stack.pop(0)
            if t:
                levelNode.append(t.val)
                if t.left:
                    stack.append(t.left)
                if t.right:
                    stack.append(t.right)
            else:
                if flag:
                    levelNode.reverse()
                    res.append(levelNode)
                    levelNode = []
                    flag = False
                else:
                    res.append(levelNode)
                    levelNode = []
                    flag = True
                if stack:
                    stack.append(None)
        return res