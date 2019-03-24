#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def get_path(path, node):
            if path == "":
                path = str(node.val)
            else:
                path = path + "->" + str(node.val)
            return path

        def dfs(node, path):
            if node is None:
                return path
            if node.left is None and node.right is None:
                path = get_path(path, node)
                paths.append(path)
                return
            path = get_path(path, node)
            if node.left is not None:
                dfs(node.left, path)
            if node.right is not None:
                dfs(node.right, path)

        paths = []
        dfs(root, "")
        return paths
