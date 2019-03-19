#!/bin/env python
# -*- coding:utf-8 -*-

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        quick, slow, pre = head, head, head
        while quick is not None and quick.next is not None:
            pre = slow
            quick = quick.next.next
            slow = slow.next

        pre.next = None
        mid = slow

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, l, r):
        dummy = ListNode(0)
        p = dummy
        while l is not None and r is not None:
            if l.val > r.val:
                p.next = r
                r = r.next
            else:
                p.next = l
                l = l.next
            p = p.next
        if l is not None:
            p.next = l
        if r is not None:
            p.next = r
        return dummy.next
