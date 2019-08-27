# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:32:35 2019

@author: LiuZiping
"""

def patition(s):
    res = []
    tempList = []
    size = len(s)
    if size <= 0:
        return None
    _backtrack(s, tempList, 0, size, res)
    return res

def ispalindrome(substring):
    left, right = 0, len(substring) - 1
    while substring[left] == substring[right] and left < right:
        left += 1
        right -= 1
    return left >= right
    
def _backtrack(s, tempList, begin, size, res):
    sliced = s[begin:]
    listStr = ""
    if len(listStr.join(tempList)) == size:
        res.append(tempList.copy())
    for i in range(len(sliced)):
        if ispalindrome(sliced[:i+1]):
            tempList.append(sliced[:i+1])
        else:
            continue
        _backtrack(s, tempList, begin + i + 1, size, res)
        tempList.pop()

if __name__ == "__main__":
    s = 'abaca'
    res = patition(s)
    