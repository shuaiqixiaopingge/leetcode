# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:53:06 2019

@author: LiuZiping
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        param: treeNode root
        param: int k
        return: int
        """
        """
        由于是二叉查找树，寻找第K小的节点等同于寻找左子树有k-1个节点的节点
        注意递归寻找时，如果其左子树的节点数量大于k-1，目标节点在其右子树上
        此时应该注意改变递归时传入的参数，相当于在其右子节点上进行重新查找
        """
        if not root:
            return None
        c = self.nodeCount(root.left)
        if c == k -1:
            return root.val
        elif c < k - 1:
            return self.kthSmallest(root.right, k-c-1)
        else:
            return self.kthSmallest(root.left, k)
    def nodeCount(self, root):
        if not root:
            return 0
        left = self.nodeCount(root.left)
        right = self.nodeCount(root.right)
        return 1 + left + right