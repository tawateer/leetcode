#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].


示例 2:
输入: [1, 2, 3, 5]
输出: false

解释: 数组不能分割成两个元素和相等的子集.
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in nums:
            for j in range(target, 0, -1):
                if j >= i:
                    dp[j] = dp[j] or dp[j-i]
        return dp[-1]

    def canPartition2(self, nums):
        if len(nums) < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        # dp[0...n][0] 为 1, 因为和为 0 不需要相加即为真.
        dp = [[1] + [0] * target for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    if dp[i][j] == 0 and dp[i-1][j-nums[i-1]] == 1:
                        dp[i][j] = 1
        return dp[-1][-1] == 1


s = Solution()
print s.canPartition2([1, 5, 11, 5])
print s.canPartition2([1, 2, 3, 5])
print s.canPartition2([1, 2, 5])
