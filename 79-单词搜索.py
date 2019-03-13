#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

"""


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if word == "":
            return True
        if len(board) == 0:
            return False

        visited = [[0] * len(board[0]) for i in xrange(0, len(board))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, board, visited, word, index):
            if word[index] != board[i][j]:
                return False
            if len(word) - 1 == index:
                return True
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]):
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        if dfs(ni, nj, board, visited, word, index + 1):
                            return True
                        visited[ni][nj] = 0
            return False

        for i in xrange(0, len(board)):
            for j in xrange(0, len(board[0])):
                visited[i][j] = 1
                if dfs(i, j, board, visited, word, 0):
                    return True
                visited[i][j] = 0
        return False


board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
s = Solution()
print s.exist(board, "ABCCED")
print s.exist(board, "SEE")
print s.exist(board, "ABCB")
