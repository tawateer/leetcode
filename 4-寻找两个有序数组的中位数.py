#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

"""

"""
偶-奇
0 1 2 3
- - *
0 1 2 3 4
- - -

偶偶
0 1 2 3 4
- - *
0 1 2 3 4
- - -

奇奇
0 1 2 3 4 5
- - - *
0 1 2 3 4 5
- - -

奇-偶
0 1 2 3 4 5
- - - *
0 1 2 3 4 5 6
- - - -
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if n == 0:
            raise ValueError

        imin, imax, left_length = 0, m, (m+n+1)/2
        while imin <= imax:
            i = (imin + imax) / 2
            j = left_length - i
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m+n) & 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right)/2.0
