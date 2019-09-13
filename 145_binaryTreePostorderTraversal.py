# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:57:05 2019

@author: LiuZiping
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        param: root treeNode
        return: List[int]
        """
        """
        后序遍历的方法：
        首先把各个父节点和其左右子节点都压入栈中
        注意出栈时，要判断其是否满足两个条件之一：
        1.为子叶节点
        2.其左右子节点都已经出栈
        """
        if not root:
            return []
        stack = [root]
        res = []
        p = root
        """
        若栈中的最后一个节点的左子节点或者右子节点已经出栈
        那么这个节点应该出栈（其左右子节点都已经出栈了）
        """
        while stack:
            top = stack[-1]
            if top.left == p or top.right == p or (top.left == None and top.right == None):
                p = stack.pop()
                res.append(p.val)
            else:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        return res 