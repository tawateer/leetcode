#!/bin/env python
# -*-  coding:utf-8 -*-

"""
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

"""

end_of_word = "#"


class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = end_of_word

    def add_word(self, word):
        node = self.root
        for i in range(len(word)):
            node = node.setdefault(word[i], {})
        node[self.end_of_word] = {}


class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of strings
    def find_words(self, board, words):
        trie = Trie()
        res = []
        visited = [[0] * len(board[0]) for i in xrange(0, len(board))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, board, visited, res, root, path):
            if not root:
                return

            if end_of_word in root:
                res.append(path)

            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    c = board[ni][nj]
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        dfs(ni, nj, board, visited, res, root.get(c, None), path + c)
                        visited[ni][nj] = 0

        for word in words:
            trie.add_word(word)
        root = trie.root
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                c = board[i][j]
                visited[i][j] = 1
                dfs(i, j, board, visited, res, root.get(c, None), c)
                visited[i][j] = 0
        return list(set(res))


board = [
  ['o', 'a', 'a', 'n'],
  ['e', 't', 'a', 'e'],
  ['i', 'h', 'k', 'r'],
  ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]
s = Solution()
print s.find_words(board, words)
