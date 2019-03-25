#!/bin/env python
# -*- coding:utf-8 -*-

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.dfs([], 0, n)
        return self.result

    def dfs(self, p, left, n):
        if len(p) == 2*n:
            self.result.append("".join(p))

        if left < n:
            p.append("(")
            self.dfs(p, left+1, n)
            p.pop()

        right = len(p) - left
        if right < left:
            p.append(")")
            self.dfs(p, left, n)
            p.pop()


s = Solution()
print s.generateParenthesis(3)
