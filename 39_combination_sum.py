# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:49:40 2019

@author: LiuZiping
"""
def combinationSum(candidates, target):
        """
        回溯法，层层递减，得到符合条件的路径就加入结果集中，超出则剪枝；
        主要是要注意一些细节，避免重复等；
        """
        size = len(candidates)
        if size <= 0:
            return []
        
        # 先排序，便于后面剪枝
        candidates.sort()
        
        path = []
        res = []
        _find_path(target, path, res, candidates, 0, size)
        
        return res
        
def _find_path(target, path, res, candidates, begin, size):
        """沿着路径往下走"""
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                    left_num = target - candidates[i]
                # 如果剩余值为负数，说明超过了，剪枝
                    if left_num < 0:
                        break
                # 否则把当前值加入路径
                path.append(candidates[i])
                # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除，
                # 因为根据他们得出的解一定在之前就找到过了
                _find_path(left_num, path, res, candidates, i, size)
                # 记得把当前值移出路径，才能进入下一个值的路径
                path.pop()

#candidates = [2,3,6,7]
#target = 7
#solution = combinationSum(candidates, target)