#!/bin/env python
# -*- coding:utf-8 -*-

"""
假设有四种面额的钱币，1 元、2 元、5 元和 10 元，
而您一共给我 10 元，那您可以奖赏我 1 张 10 元，
或者 10 张 1 元，或者 5 张 1 元外加 1 张 5 元等等。

如果考虑每次奖赏的金额和先后顺序，那么最终一共有多少种不同的奖赏方式呢？

"""

import copy


class Solution(object):
    def __init__(self):
        self.total = 10
        self.result = []

    def _findTarget(self, nums, one_result, remain):
        if remain == 0:
            self.result.append(one_result)
            return

        for i in nums:
            if remain >= i:
                o = copy.deepcopy(one_result)
                o.append(i)
                self._findTarget(nums, o, remain - i)

    def findTarget(self, nums):
        self._findTarget(nums, [], self.total)
        return self.result


s = Solution()
print s.findTarget([1, 2, 5, 10])
