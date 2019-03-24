#!/bin/env python
#-*- coding:utf-8 -*-\
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(node, path):
            if node is None:
                return path
            if node.left is None and node.right is None:
                paths.append(path + [node.val])
                return
            path = path + [node.val]
            if node.left is not None:
                dfs(node.left, path)
            if node.right is not None:
                dfs(node.right, path)

        paths = []
        dfs(root, [])

        result = []
        for p in paths:
            if sum(p) == s:
                result.append(p)
        return result
