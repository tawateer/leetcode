#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.r(root, 0)
        return min(self.result)

    def r(self, node, num):
        if not node:
            self.result.append(num)
        else:
            num += 1
            self.r(node.left, num)
            self.r(node.right, num)
