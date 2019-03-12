#!/bin/env python
# -*- coding: utf-8 -*-

"""

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


def find(s):
    max_length = 0

    start = 0
    m = {}
    for i in xrange(len(s)):
        if s[i] not in m or m[s[i]] < start:
            m[s[i]] = i
            if max_length < i - start + 1:
                max_length = i - start + 1
        else:
            start = m[s[i]] + 1
            m[s[i]] = i

    return max_length


print find("abcabcbb")
print find("bbbbb")
print find("pwwkew")
