#!/bin/env python
# -*- coding: utf-8 -*-

"""

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 10000。

示例 1:

输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
示例 2:

输入:
s = "AABABBA", k = 1

输出:
4

解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

"""


def replace(s, k):
    max_length = 0

    j = 0
    i = 0
    win_map = {}
    while j < len(s):
        win_map[s[j]] = win_map.get(s[j], 0) + 1
        if j >= k:
            x = sorted(win_map.items(), lambda x, y: cmp(x[1], y[1]))[-1]
            win_max_value = x[1]

            if j - i + 1 - win_max_value == k:
                if max_length < j - i + 1:
                    max_length = j - i + 1
            elif j - i + 1 - win_max_value > k:
                win_map[s[i]] = win_map[s[i]] - 1
                i += 1

        j += 1

    return max_length


print replace("ABAB", 2)
print replace("AABABBA", 1)
print replace("AABABBDDDDDVDDA", 2)

