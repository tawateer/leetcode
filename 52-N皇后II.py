#!/bin/env python
# -*- coding:utf-8 -*-

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):
    def totalNQueens(self, n):
        def dfs(path, n):
            if len(path) == n:
                return 1
            res = 0
            for i in range(n):
                if i not in path and isValidQueen(path, i):
                    path.append(i)
                    res += dfs(path, n)
                    path.pop()
            return res

        def isValidQueen(path, k):
            for i in range(len(path)):
                if abs(k - path[i]) == abs(len(path) - i):
                    return False
            return True

        return dfs([], n)


s = Solution()
print s.totalNQueens(4)
print s.totalNQueens(8)
