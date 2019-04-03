#!/bin/env python
# -*- coding:utf-8 -*-

"""
    二分查找算法: 递增数组
"""


# 查找给定值的下标(数组没有重复元素)
def find_target_index(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


# 查找第一个值等于给定值的下标
def find_target_first_index(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

    if low < len(nums) and nums[low] == target:
        return low
    else:
        return -1


# 查找最后一个值等于给定值的下标
def find_target_last_index(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            if (mid == len(nums)-1) or (nums[mid+1] != target):
                return mid
            else:
                low = mid + 1
    return -1


# 查找第一个大于等于给定值的下标
def find_target_greater_and_equal_first_index(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= target:
            if (mid == 0) or (nums[mid - 1] < target):
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


# 查找最后一个小于等于给定值的下标
def find_target_less_and_equal_last_index(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        else:
            if (mid == len(nums)-1) or (nums[mid+1] > target):
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == "__main__":
    print find_target_index([1, 2, 3, 4, 5], 4)
    print find_target_first_index([1, 2, 3, 4, 4, 4, 5], 4)
    print find_target_last_index([1, 2, 3, 4, 4, 4, 5], 4)
    print find_target_greater_and_equal_first_index([1, 2, 3, 4, 4, 4, 5], 3)
    print find_target_less_and_equal_last_index([1, 2, 3, 4, 4, 4, 5], 4)
