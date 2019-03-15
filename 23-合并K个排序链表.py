#!/bin/env python
# -*- coding:utf-8 -*-

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""

import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = []
        p = dummy = ListNode(-1)
        for i in xrange(len(lists)):
            node = lists[i]
            if not node:
                continue
            heapq.heappush(heap, (node.val, node))

        while heap:
            val, node = heapq.heappop(heap)

            p.next = node
            p = p.next

            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))

        return dummy.next

