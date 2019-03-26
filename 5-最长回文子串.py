#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        length = len(s)

        dp = [[0] * length for i in range(length)]
        for i in range(length):
            dp[i][i] = 1

        import sys
        result = -sys.maxint
        target = ""
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 0
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = 0
                if dp[i][j] and result < dp[i][j]:
                    result = dp[i][j]
                    target = s[i:j + 1]

        return target if target != "" else s[0]
