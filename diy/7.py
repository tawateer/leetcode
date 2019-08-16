#!/bin/env python
# -*- coding:utf-8 -*-

"""
假设, 已知一个出栈的序列，求所有可能的入栈序列。
"""


import copy


class Solution(object):
    def __init__(self, nums):
        self.results = []
        self.nums = nums

    def _stack(self, s, result, i):
        if len(result) == len(self.nums):
            self.results.append(result)
            return

        if len(s) == 0 and i < len(self.nums):
            ns = copy.deepcopy(s)
            nresult = copy.deepcopy(result)
            ns.append(self.nums[i])
            self._stack(ns, nresult, i+1)
            return
        else:
            ns = copy.deepcopy(s)
            nresult = copy.deepcopy(result)
            if i < len(self.nums):
                ns.append(self.nums[i])
                self._stack(ns, nresult, i+1)
            ns = copy.deepcopy(s)
            nresult = copy.deepcopy(result)
            if len(ns) != 0:
                nresult.append(ns.pop())
                self._stack(ns, nresult, i)

    def stack(self):
        self._stack([], [], 0)
        return self.results


x = Solution([1, 2, 3, 4])
r = x.stack()
print len(r)
for i in r:
    print i
