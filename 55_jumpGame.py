# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:12:14 2019

@author: LiuZiping
"""

def jumpGame(nums):
    """
    param:nums List[int]
    return: bool#if __name__ == "__main__":
#    nums = [3,2,1,0,4]
#    result = jumpGame(nums)
    """
    if len(nums) <= 0:
        return None
    jumpMax = 0
    for i in range(len(nums)):
        if jumpMax < i:
            return False
        #如果当前的位置不能到达，说明不能遍历数组
        jumpMax = max(nums[i] + i, jumpMax)
        #更新能到达的最大索引
    return jumpMax >= len(nums) - 1

