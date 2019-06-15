#!/bin/env python
# -*- coding:utf-8 -*-

"""
假设有一个 4 位字母密码，每位密码是 a～e 之间的小写字母。

你能否编写一段代码，来暴力破解该密码？

（提示：根据可重复排列的规律，生成所有可能的 4 位密码。）

"""


class Solution(object):
    def __init__(self):
        self.items = ["a", "b", "c", "d", "e"]
        self.length = 4
        self.result = []

    def _mySolve(self, curr):
        if len(curr) == self.length:
            self.result.append(curr)
        else:
            for i in self.items:
                self._mySolve(curr + i)

    def mySolve(self):
        self._mySolve("")
        return self.result


s = Solution()
print s.mySolve()
