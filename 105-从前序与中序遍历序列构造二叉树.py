#!/bin/env python
# -*- coding:utf-8 -*-

"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        看一下前序和中序有什么特点，前序 1,2,4,7,3,5,6,8 ，中序 4,7,2,1,5,3,8,6

        有如下特征：
        前序中左起第一位1肯定是根结点，我们可以据此找到中序中根结点的位置rootin;
        中序中根结点左边就是左子树结点，右边就是右子树结点，即[左子树结点，根结点，右子树结点]，我们就可以得出左子树结点个数为int left = rootin - leftin;
        前序中结点分布应该是：[根结点，左子树结点，右子树结点];
        根据前一步确定的左子树个数，可以确定前序中左子树结点和右子树结点的范围;
        如果我们要前序遍历生成二叉树的话，下一层递归应该是:
        左子树：root->left = pre_order(前序左子树范围，中序左子树范围，前序序列，中序序列);
        右子树：root->right = pre_order(前序右子树范围，中序右子树范围，前序序列，中序序列);
        每一层递归都要返回当前根结点root.
        """
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        # print(preorder, inorder)
        x = inorder.index(root.val)   # 找到根在中序中的位置
        root.left = self.buildTree(preorder[1:x+1], inorder[0:x])
        root.right = self.buildTree(preorder[x+1:], inorder[x+1:])
        return root
