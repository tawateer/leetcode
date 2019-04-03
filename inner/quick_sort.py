#!/bin/env python
# -*- coding:utf-8 -*-


import random


def quick_sort(nums):
    _quick_sort_between(nums, 0, len(nums)-1)


def _quick_sort_between(nums, low, high):
    if low < high:
        # get a random position as the pivot
        k = random.randint(low, high)
        nums[low], nums[k] = nums[k], nums[low]

        m = _partition(nums, low, high)  # nums[m] is in final position
        _quick_sort_between(nums, low, m - 1)
        _quick_sort_between(nums, m + 1, high)


def _partition(nums, low, high):
    pivot, j = nums[low], low
    for i in range(low + 1, high + 1):
        if nums[i] <= pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]  # swap
    nums[low], nums[j] = nums[j], nums[low]
    return j
