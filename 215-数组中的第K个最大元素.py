#!/bin/env python
# -*-  coding:utf-8 -*-

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

"""


import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        data = nums[0:k]
        heapq.heapify(data)

        for i in range(k, len(nums)):
            if nums[i] >= data[0]:
                heapq.heapreplace(data, nums[i])
        return data[0]

    def findKthLargest2(self, nums, k):
        def partition(nums, p, r):
            pivot = nums[r]
            i, j = p, p
            while j < r:
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def findKthLargest(nums, p, r, k):
            x = partition(nums, p, r)
            if x + 1 == k:
                return nums[x]
            elif x + 1 > k:
                return findKthLargest(nums, 0, x-1, k)
            elif x + 1 < k:
                return findKthLargest(nums, x+1, r, k)
            else:
                return -1

        return findKthLargest(nums, 0, len(nums)-1, k)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution()
print s.findKthLargest2(nums, k)
