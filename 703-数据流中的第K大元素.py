#!/bin/env python
# -*-  coding:utf-8 -*-


"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。

"""


import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.data = nums
        heapq.heapify(self.data)
        while len(self.data) > self.k:
            heapq.heappop(self.data)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.data) < self.k:
            heapq.heappush(self.data, val)
        elif self.data[0] < val:
            heapq.heapreplace(self.data, val)
        return self.data[0]


k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest(3, arr)
print kthLargest.add(3)
print kthLargest.add(5)
print kthLargest.add(10)
print kthLargest.add(9)
print kthLargest.add(4)
