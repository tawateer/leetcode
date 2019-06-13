#!/bin/env python
# -*- coding:utf-8 -*-

"""
在 1 到 n 的数字中，有且只有唯一的一个数字 m 重复出现了，其它的数字都只出现一次。请把这个数字找出来、

"""


class Solution(object):
    def findDuplicate(self, nums):
        target = 0
        for i in nums:
            target ^= i
        for i in range(1, len(nums)):
            target ^= i
        return target

s = Solution()
print s.findDuplicate([1, 2, 3, 4, 4])
print s.findDuplicate([1, 2, 2, 3, 4])
