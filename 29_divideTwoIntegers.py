# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:36:44 2019

@author: LiuZiping
"""

def devision(divided, divisor):
    """
    :param int divided
    :param int divisor
    :return int result
    """
    if divisor == 0:
        return ZeroDivisionError
    sign = (divided >= 0) == (divisor > 0)
    absDivided = abs(divided)
    absDivisor = abs(divisor)
    result = 0
    """
    此题本质上是有序数组求值
    利用二分查找的思想
    """
    while absDivisor <= absDivided:
        r, absDivided = absDivision(absDivided, absDivisor)
        result += r
    result = result if sign else -result
    return max(-2**31+1, min(2**31, result))

def absDivision(absDivided, absDivisor):
    """
    翻倍除法，如果可以被除，则下一步除数翻倍，直至除数大于被除数；
    返回商加总的结果和被除数的剩余值
    :param int absDivided
    :param int abdDivisor
    :return tuple, left_absDivided
    """
    timeCount = 1
    result = 0
    while absDivisor <= absDivided:
        absDivided -= absDivisor
        result += timeCount
        absDivisor += absDivisor
        timeCount += timeCount
    return result, absDivided

#if __name__ == "__main__":
#    divided = 10
#    divisor = -3
#    result = devision(divided, divisor)
    