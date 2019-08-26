# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:55:20 2019

@author: LiuZiping
"""

def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        down_index = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                down_index = i
                break
        if down_index == None:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, down_index, -1):
                if nums[i] > nums[down_index]:
                    nums[down_index], nums[i] = nums[i], nums[down_index]
                    break
            i, j= down_index + 1, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums

#nums = [1,2,3]
#nextPermutation(nums)