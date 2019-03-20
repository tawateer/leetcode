#!/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        dp[i][j][0] 表示第 i 天交易 j 次当天没有股票的最大收益;
        dp[i][j][1] 表示第 i 天交易 j 次当天拥有股票的最大收益;
        最终最大收益是 dp[n-1][0...k][0] 的值.
        
        dp[i][j][0] = max(
            dp[i-1][j][0],
            dp[i-1][j-1][1] + prices[i]                
        )
    
         dp[i][j][1] = max(
            dp[i-1][j][1],
            dp[i-1][j][0] - prices[i]                
        )
        """
        import sys

        n = len(prices)
        if n == 0:
            return 0
        if k == 0:
            return 0
        k = min(k, n/2)

        result = 0

        # dp 三维数组.
        dp = []
        for i in range(len(prices)):
            m = []
            for j in range(k+1):
                n = [-sys.maxint, -sys.maxint]
                m.append(n)
            dp.append(m)

        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(0, k+1):
                # print i, j
                if j == 0:
                    dp[i][j][0] = dp[i-1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])

                result = max(dp[i][j][0], result)

        return result


s = Solution()
print s.maxProfit(2, [3, 2, 6, 5, 0, 3])
print s.maxProfit(2, [2, 4, 1])
print s.maxProfit(2, [2, 6, 1, 7])
print s.maxProfit(2, [2, 1, 0, 10])
