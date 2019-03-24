#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(subset, index, nums):
            result.append(subset)

            for i in range(index, len(nums)):
                dfs(subset+[nums[i]], i+1, nums)

        result = []
        dfs([], 0, nums)
        return result


s = Solution()
print s.subsets([1, 2, 3])
