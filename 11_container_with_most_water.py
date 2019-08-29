# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:18:46 2019

@author: LiuZiping
"""

def containerWithMostWater(height):
    length = len(height)
    if length <= 1:
        return 0
    left, right = 0, length - 1
    area = 0
    while left < right:
        area = max(area, min(height[left], height[right])*(right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area

#if __name__ == "__main__":
#    height = [1,8,6,2,5,4,8,3,7]
#    area = containerWithMostWater(height)