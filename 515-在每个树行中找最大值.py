#!/bin/env python
# -*- coding:utf-8 -*-

"""
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        import sys
        nodes = [root]
        result = []

        while nodes:
            max_value = -sys.maxint
            for i in range(len(nodes)):
                node = nodes.pop(0)
                max_value = max(max_value, node.val)
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            result.append(max_value)
        return result







