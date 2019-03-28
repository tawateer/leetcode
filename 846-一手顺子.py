#!/bin/env python
# -*- coding:utf-8 -*-

"""
爱丽丝有一手（hand）由整数数组给定的牌。

现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。

如果她可以完成分组就返回 true，否则返回 false。

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。

示例 2：
输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。

提示：
1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        # if len(hand) < W * W:
        #     return False

        import collections
        n = len(hand)
        if n == 0 or (n and n % W != 0):
            return False
        cnt = collections.Counter(hand)
        hand.sort()
        for i in hand:
            if i in cnt:
                for k in range(i, i+W):
                    if k not in cnt:
                        return False
                    cnt[k] -= 1
                    if cnt[k] == 0:
                        del cnt[k]
        return True


s = Solution()
print s.isNStraightHand([1, 2, 2, 3, 3, 4, 6, 7, 8], 3)
print s.isNStraightHand([1, 2, 3, 4, 5], 4)
print s.isNStraightHand([1, 2, 3, 4, 5, 6], 2)
