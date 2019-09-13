# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:13:38 2019

@author: LiuZiping
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        param: treeNode root
        return List[List[int]]
        """
        """
        层序遍历注意添加一个None标识符
        将该层的所有节点的子节点全部压入栈中，并从栈首取出节点
        当该层的所有节点都遍历过后，在栈中添加NOne标识符
        当None标识符出栈时，代表该层已经遍历完全
        """
        if not root:
            return []
        res = []
        stack = [root, None]
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
                res.append(levelNode)
                levelNode = []
                if stack:
                    stack.append(None)
        return res