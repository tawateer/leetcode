#!/bin/env python
# -*- coding:utf-8 -*-

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

"""


class Solution(object):
    def solveNQueens(self, n):
        ans = []

        def dfs(path, n, ans):
            if len(path) == n:
                ans.append(drawChess(path))
                return

            for i in range(n):
                if i not in path and isValidQueen(path, i):
                    path.append(i)
                    dfs(path, n, ans)
                    path.pop()

        def isValidQueen(path, k):
            for i in range(len(path)):
                if abs(k - path[i]) == abs(len(path) - i):
                    return False
            return True

        def drawChess(path):
            ret = []
            chess = [["."] * len(path) for _ in range(len(path))]
            for i in range(0, len(path)):
                chess[i][path[i]] = "Q"
            for chs in chess:
                ret.append("".join(chs))
            return ret

        dfs([], n, ans)
        return ans


s = Solution()
print s.solveNQueens(4)
print s.solveNQueens(8)
