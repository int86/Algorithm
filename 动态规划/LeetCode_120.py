#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 120. 三角形最小路径和  难度：中等
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = [[0 for j in range(len(i))] for i in triangle]
        dp[0][0] = triangle[0][0]
        #处理左边边
        for i in range(1,len(triangle)):
            dp[i][0] += dp[i-1][0] + triangle[i][0]
        #处理右边边
        for j in range(1,len(triangle)):
            dp[j][-1] += dp[j-1][-1] + triangle[j][-1]
        #处理中间
        if len(triangle)>2:
            for i in range(2,len(triangle)):
                for j in range(1,len(triangle[i])-1):
                    dp[i][j] += min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        return min(dp[-1])