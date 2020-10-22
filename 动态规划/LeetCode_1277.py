#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1277. 统计全为 1 的正方形子矩阵 难度：中等
# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

 

# 示例 1：

# 输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释： 
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
# 示例 2：

# 输入：matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。 
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m,n,ans = len(matrix),len(matrix[0]),0
        dp = [[0 for i in range(n)] for x in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
            ans = ans + dp[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
            ans = ans +dp[0][j]
        if matrix[0][0] == 1:
            ans = ans - 1
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
                    ans = ans + dp[i][j]
        return ans  