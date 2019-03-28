#!/bin/env pythonn
# -*- coding:utf-8 -*-

"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution(object):
    def countPrimes(self, n):
        """
            这题搜到一个非常牛逼的算法,叫做厄拉多塞筛法.
            比如说求 20 以内质数的个数,首先 0,1 不是质数.
            2 是第一个质数,然后把 20 以内所有 2 的倍数划去.
            2 后面紧跟的数即为下一个质数 3, 然后把 3 所有的倍数划去.
            3 后面紧跟的数即为下一个质数 5, 再把 5 所有的倍数划去.
            以此类推.

        """
        if n < 3:
            return 0
        else:
            # 首先生成了一个全部为1的列表
            output = [1] * n
            # 因为0和1不是质数,所以列表的前两个位置赋值为0
            output[0], output[1] = 0, 0
            # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
            # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
            for i in range(2, int(n**0.5)+1):
                if output[i] == 1:
                    output[i*i:n:i] = [0] * len(output[i*i:n:i])
        # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
        return sum(output)

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        if n == 2:
            return 0

        result = 0

        import math
        for i in range(2, n):
            ok = True
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    ok = False
                    break
            if ok:
                result += 1

        return result


s = Solution()
s.countPrimes(20)
