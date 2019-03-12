#!/bin/env python
# -*- coding: utf-8 -*-

"""

给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

"""


def find(s, t):
    res = ""
    min_length = 99999
    full_score = len(t)

    meta_map = {}
    for i in xrange(len(t)):
        meta_map[t[i]] = meta_map.get(t[i], 0) + 1
    # print meta_map

    tmp_dict = {}
    score = 0
    i = 0
    j = 0
    while j < len(s):
        if s[j] not in meta_map:
            j += 1
            continue

        tmp_dict[s[j]] = tmp_dict.get(s[j], 0) + 1
        if tmp_dict[s[j]] <= meta_map[s[j]]:
            score += 1

        if score == full_score:
            while i <= j:
                if s[i] not in meta_map:
                    i += 1
                    continue

                if tmp_dict[s[i]] == meta_map[s[i]]:
                    if min_length > j - i + 1:
                        min_length = j - i + 1
                        res = s[i:i+min_length]

                    tmp_dict[s[i]] = tmp_dict[s[i]] - 1
                    score -= 1
                    i += 1
                    break

                tmp_dict[s[i]] = tmp_dict[s[i]] - 1
                i += 1
        j += 1

    return res


print find("ADOBECODEBANC", "ABC")
