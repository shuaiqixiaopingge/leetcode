# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:14:59 2019

@author: LiuZiping
"""

def subset_ii(nums):
    res = []
    subset = []
    size = len(nums)
    if size <= 0:
        return None
    nums.sort()
    _backtrack(nums, subset, 0, size, res)
    return res
def _backtrack(nums, subset, begin, size, res):
    res.append(subset.copy())
    for i in range(begin, size):
        if i > begin and nums[i] == nums[i-1]:
            continue
        subset.append(nums[i])
        _backtrack(nums, subset, i+1, size, res)
        subset.pop()
        
if __name__ == "__main__":
    nums = [1,2,1,2,1,2]
    res = subset_ii(nums)