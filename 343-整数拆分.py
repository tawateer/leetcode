#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""
"""
    http://jalan.space/leetcode-notebook/offer/cut-rope.html
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        res_dict = dict()
        res_dict[0] = 0
        res_dict[1] = 1
        res_dict[2] = 2
        res_dict[3] = 3

        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                tmp = res_dict[j] * res_dict[i - j]
                if i not in res_dict:
                    res_dict[i] = tmp
                else:
                    if tmp > res_dict[i]:
                        res_dict[i] = tmp

        return res_dict[n]
