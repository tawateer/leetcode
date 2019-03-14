#!/bin/env python
# -*-  coding:utf-8 -*-

"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def r(node):
            if not node:
                return

            result.append(node.val)
            if node.left:
                r(node.left)
            if node.right:
                r(node.right)

        r(root)
        return result
