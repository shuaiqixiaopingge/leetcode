# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:01:08 2019

@author: LiuZiping
"""
import collections
def groupAnagrams(strs):
    """
    param: List[str]
    return: List[List[str]]
    """
    str_dict = collections.defaultdict(list)
    for s in strs:
        strs_keys = [0]*26
        for c in s:
            strs_keys[ord(c) - ord('a')] += 1
        str_dict[tuple(strs_keys)].append(s)
        """
        字典的keys不可以用list只能用tuple
        """
    return str_dict.values()

#if __name__ == "__main__":
#    strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
#    result = groupAnagrams(strs)