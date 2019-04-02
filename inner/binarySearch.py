#!/bin/env python
# -*- coding:utf-8 -*-

"""
    二分查找算法: 递增数组
"""


# 查找某个数的下标
def find_index(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


print find_index([1, 2, 3, 4], 3)
print find_index([1, 2, 2, 4], 3)


# 查找第一个大于等于某个数的下标
def find_first_not_less_index(nums, target):
    left = 0
    right = len(nums)-1
    if target > nums[right]:
        return -1
    if target < nums[left]:
        return -1
    while left < right:
        mid = left + ((right - left) >> 1)
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


print find_first_not_less_index([1, 2, 3, 4], 3)
print find_first_not_less_index([1, 2, 3, 3, 4], 4)
print find_first_not_less_index([1, 2, 3, 3, 4], 5)
print find_first_not_less_index([1, 2, 3, 3, 4], 0)


# 查找第一个大于某个数的下标
def find_first_greater_index(nums, target):
    left = 0
    right = len(nums)-1
    if target >= nums[right]:
        return -1
    if target < nums[left]:
        return left
    while left < right:
        mid = left + ((right - left) >> 1)
        if target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


print find_first_greater_index([1, 2, 3, 4], 3)
print find_first_greater_index([1, 2, 3, 3, 4], 4)
print find_first_greater_index([1, 2, 3, 3, 4], 5)
print find_first_greater_index([1, 2, 3, 3, 4], 2)
