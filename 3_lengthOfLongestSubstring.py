# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:29:53 2019

@author: LiuZiping
"""

def lenggthOfLongesrSubstring(s):
    length = len(s)
    if length <= 0:
        return None
    i,j = 0, 1
    res = s[0]
    hashmap = [s[0]]
    while j < length:
        if s[j] in hashmap:
            hashmap.remove(s[i])
            i += 1
        else:
            hashmap.append(s[j])
            j += 1
            if j - i > len(res):
                res = s[i:j]
    return len(res)

#if __name__ == "__main__":
#    s = "ppkeww"
#    res = lenggthOfLongesrSubstring(s)
    