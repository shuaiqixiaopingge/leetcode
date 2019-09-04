# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:57:26 2019

@author: LiuZiping
"""

def searchInRotatedSortedArray(nums, target):
    """
    param: List[int]
    target: int
    return: int
    """
    if len(nums) <= 0:
        return None
    left = 0
    right = len(nums) - 1
    while left <= right :
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if nums[left] <= nums[right]:
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] >= nums[left]:
            """
            数组的mid值比左端的值大说明数组的左端是有序排列的, 
            如果target的mid值小，且target比left值大，说明target在左端有序的数组范围内
            反之，target落在数组的右半侧
            """
            if target < nums[mid] and target >= nums[left]:
               right = mid - 1
            else:
                left = mid + 1
        else:
            """
            数组的mid值比左端小说明说明的右端是有序排列的
            如果target比mid值大，且target比right值小，说明target 在右端有序的数组范围之内
            反之，target落在数组的左半侧
            """
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

#if __name__ == "__main__":
#    nums = [3,5,1]
#    location = searchInRotatedSortedArray(nums, 3)
#    