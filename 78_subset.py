# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:43:11 2019

@author: LiuZiping
"""
def subSet(nums):
    res = []
    subset = []
    if len(nums) == 0:
        return res.append(nums)
    size = len(nums)
    _backtrack(nums,subset, 0, size, res)
    return res

def _backtrack(nums, subset, begin, size, res):
    res.append(subset.copy())
    for i in range(begin, size):
        subset.append(nums[i])
        _backtrack(nums, subset, i+1, size, res)
        subset.pop()

#nums = []
#res = subSet(nums)