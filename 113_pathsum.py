# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:51:24 2019

@author: LiuZiping
"""

class treeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def pathSum(root, target):
    res = []
    path = []
    if not root:
        return None
    _backtrack(root, target, path, res)
    return res
def _backtrack(root, target, path, res):
    if root == None:
        return 
    path.append(root.val)
    if target - root.val == 0 and root.left == None and root.right == None:
        res.append(path.copy())
    else:
        _backtrack(root.left, target - root.val, path, res)
        _backtrack(root.right, target - root.val, path, res)
    path.pop()

if __name__ == "__main__":
    node0 = treeNode(5)
    node00 = treeNode(4)
    node01 = treeNode(8)
    node0.left = node00
    node0.right = node01
    node000 = treeNode(11)
    node010 = treeNode(13)
    node011= treeNode(4)
    node00.left = node000
    node01.left = node010
    node01.right = node011
    node0000 = treeNode(7)
    node0001 = treeNode(2)
    node0110 = treeNode(5)
    node0111 = treeNode(1)
    node000.left = node0000
    node000.right = node0001
    node011.left = node0110
    node011.right = node0111
    res = pathSum(node0, 22)