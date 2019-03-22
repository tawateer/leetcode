#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
"""


class Solution(object):
    def _leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        import heapq

        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += heap and n or cnt  # == if heap then n else cnt
        return ans

    # O(n) # of the most frequent tasks, say longest, will determine the legnth
    # to void counting idle intervals, we count (longest - 1) * (n + 1)
    # then count how many will in the last cycle which means finding ties
    # if counted number is less than # of tasks which means
    # less frequent tasks can be always placed in such cycle
    # and it won't cause any conflicts with requirement since even most frequent can be settle
    # finally, return max(# of task, total counted number)
    def leastInterval(self, tasks, n):
        import collections

        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        for count in counts:
            ans += count == longest and 1 or 0
        return max(len(tasks), ans)
