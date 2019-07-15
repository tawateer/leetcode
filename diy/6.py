#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个 int 数组 A，数组中元素互不重复，给定一个数 x，求所有求和能得到 x 的数字组合，组合中的元素来自 A，可重复使用。
例子：A = [3,2,6,7]    x = 7
输出结果：[[7], [2,2,3]]
"""

import copy


class Solution(object):
    def __init__(self):
        self.result = []

    def _t(self, nums, target, res):
        if target == 0:
            self.result.append(res)
            return

        for i in nums:
            if i <= target:
                new_result = copy.deepcopy(res)
                new_result.append(i)
                self._t(nums, target - i, new_result)

    def target_sum(self, nums, target):
        self._t(nums, target, [])
        return self.result


s = Solution()
print s.target_sum([3, 2, 7, 6], 7)
