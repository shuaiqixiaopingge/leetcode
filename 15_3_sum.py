# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:05:40 2019

@author: LiuZiping
"""

def threeSum(nums):
    length = len(nums)
    if length <= 2:
        return None
    res = []
    nums.sort()
    for i in range(length - 2):
        if nums[i] == nums[i - 1]:
            continue
        tmp = nums[i+1:]
        ans = -nums[i]
        left, right = 0, len(tmp) - 1
        while left < right:
            if tmp[left] + tmp [right] > ans:
                right -= 1
            elif tmp[left] + tmp[right] < ans:
                left += 1
            else:
                if left != 0 and right != len(tmp) - 1:
                    if tmp[left] == tmp [left - 1] or tmp[right] == tmp[right + 1]:
                        left += 1
                        right -= 1
                        continue
                sumList = [tmp[left], tmp[right], -ans]
                res.append(sumList)
                left += 1
                right -= 1
    return res
if __name__ == "__main__":
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    res = threeSum(nums)