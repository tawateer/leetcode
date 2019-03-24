#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


class Solution(object):
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        dp[i] 定义为以 nums[i] 结尾的最大子串的长度
        
        dp[i] 的值应该是 dp[0]...dp[i-1] 的最大值, 且 nums[0]...nums[i-1] 小于 nums[i] 时相应 dp 值要 +1
        
        最终的解是 max(dp[0], ..., dp[len(nums)-1])
        """

        if len(nums) <= 1:
            return len(nums)

        result = 1
        dp = [1]

        for i in range(1, len(nums)):
            max_length = 0
            for j in range(len(dp)):
                if nums[j] < nums[i]:
                    max_length = max(max_length, dp[j] + 1)
            if max_length == 0:
                dp.append(1)
            else:
                dp.append(max_length)

            result = max(result, max_length)

        return result


s = Solution()
print s.lengthOfLIS1([10, 9, 2, 5, 3, 7, 101, 18])
