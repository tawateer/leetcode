#!/bin/env python
# -*- coding:utf-8 -*-


def merge_sort(nums):
    _merge_sort_between(nums, 0, len(nums) - 1)


def _merge_sort_between(nums, low, high):
    # The indices are inclusive for both low and high.
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(nums, low, mid)
        _merge_sort_between(nums, mid + 1, high)
        _merge(nums, low, mid, high)


def _merge(nums, low, mid, high):
    # nums[low:mid], nums[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(nums[start:end + 1])
    nums[low:high + 1] = tmp
