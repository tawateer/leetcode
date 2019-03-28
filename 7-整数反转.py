#!/bin/env python
# -*- coding:utf-8 -*-

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            return -self.reverse(abs(x))

        result = 0
        while x:
            k = x % 10
            result = result * 10 + k
            x = x // 10

        return 0 if result >= 0x7fffffff else result


s = Solution()
print s.reverse(120)
print s.reverse(123)
print s.reverse(-123)
