#!/bin/env python
# -*-  coding:utf-8 -*-

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        # 去重解决重复解的问题.
        nums.sort()
        result = set()
        for i, x in enumerate(nums[:-2]):
            if i > 1 and x == nums[i-1]:
                continue

            data = {}
            for y in nums[i+1:]:
                if -x-y in data:
                    result.add((x, -x-y, y))
                else:
                    data[y] = None

        return map(list, result)

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result


s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])
