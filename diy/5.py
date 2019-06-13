#!/bin/env python
# -*- coding:utf-8 -*-

"""
有 t1，t2 … tn 个元素，不重复，从中选出两个元素(集合，不考虑顺序)，列出所有选法？

"""


class Solution(object):
    def __init__(self):
        self.result = []

    def _mySort(self, items, i):
        for j in range(i+1, len(items)):
            self.result.append(
                {items[i], items[j]}
            )

    def mySqrt(self, items):
        for i in range(len(items)):
            self._mySort(items, i)
        return self.result


s = Solution()
print s.mySqrt([1, 2, 3, 4, 5, 6])
