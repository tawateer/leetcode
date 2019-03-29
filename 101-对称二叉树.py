#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(p, q):
            if p is None:
                return q is None
            if q is None:
                return p is None
            if p.val == q.val:
                return f(p.left, q.right) and f(p.right, q.left)
            if p.val != q.val:
                return False
        if root is None:
            return True
        return f(root.left, root.right)

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        flag = -1
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == flag:
                    level.append(flag)
                    continue
                else:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(-1)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(-1)

            i = 0
            j = len(level) - 1
            while i < j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1

        return True
