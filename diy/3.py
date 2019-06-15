#!/bin/env python
# -*- coding:utf-8 -*-

"""
一个整数可以被分解为多个整数的乘积，例如，6 可以分解为 2x3。

请使用递归编程的方法，为给定的整数 n，找到所有可能的分解（1 在解中最多只能出现 1 次）。

例如，输入 8，输出是可以是 1x8, 8x1, 2x4, 4x2, 1x2x2x2, 1x2x4, ……

"""

import copy


class Solution(object):
    def __init__(self):
        self.result = []

    def _mySlove(self, x, res):
        if x == 1:
            self.result.append(res)

        for i in xrange(1, x+1):
            match = False
            if i == 1:
                if 1 not in res:
                    match = True
            else:
                if x % i == 0:
                    match = True
            if match:
                t = copy.deepcopy(res)
                t.append(i)
                self._mySlove(x // i, t)

    def mySlove(self, x):
        self._mySlove(x, [])
        return self.result


s = Solution()
print s.mySlove(8)
