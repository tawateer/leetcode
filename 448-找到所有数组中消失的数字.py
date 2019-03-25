#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                i -= 1
            i += 1

        result = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result

    def findDisappearedNumbers2(self, nums):
        result = []
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result


s = Solution()
print s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
print s.findDisappearedNumbers2([4, 3, 2, 7, 8, 2, 3, 1])
