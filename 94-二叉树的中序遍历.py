#!/bin/env python
# -*-  coding:utf-8 -*-

"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def r(node):
            if not node:
                return []
            result = []
            if node.left:
                result += r(node.left)
            result += [node.val]
            if node.right:
                result += r(node.right)
            return result
        return r(root)
