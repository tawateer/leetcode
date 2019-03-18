#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""

import copy


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, dx = [nums[0]], [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp.append(max(dp[i - 1] * nums[i], nums[i]))
                dx.append(min(dx[i - 1] * nums[i], nums[i]))
            else:
                dp.append(max(dx[i - 1] * nums[i], nums[i]))
                dx.append(min(dp[i - 1] * nums[i], nums[i]))
        return max(dp)


s = Solution()
print s.maxProduct([2, 3, -2, 4])
print s.maxProduct([-2, 0, -1])
