#!/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

"""


def find1(s, t):
    result = []

    t_length = len(t)
    meta_map = {}
    for i in xrange(t_length):
        meta_map[t[i]] = meta_map.get(t[i], 0) + 1
    # print meta_map

    i = 0
    tmp_map = {}
    while i < len(s):
        tmp_map[s[i]] = tmp_map.get(s[i], 0) + 1

        if i >= t_length:
            tmp_map[s[i-t_length]] -= 1
            if tmp_map[s[i-t_length]] == 0:
                del tmp_map[s[i-t_length]]

        if tmp_map == meta_map:
            result.append(i-t_length+1)

        i += 1

    return result


def find2(s, p):
    from collections import Counter
    s_len, p_len = len(s), len(p)
    count = p_len
    pChar = Counter(p)

    result = []
    for i in range(s_len):
        if pChar[s[i]] >= 1:
            count -= 1
        pChar[s[i]] -= 1
        if i >= p_len:
            if pChar[s[i - p_len]] >= 0:
                count += 1
            pChar[s[i - p_len]] += 1
        if count == 0:
            result.append(i - p_len + 1)

    return result


print find1("cbaebabacd", "abc")
print find1("abab", "ab")
print "=" * 20
print find2("cbaebabacd", "abc")
print find2("abab", "ab")
