#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 931. 下降路径最小和 难度：中等
# 给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

# 下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

 

# 示例：

# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：12
# 解释：
# 可能的下降路径有：
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 和最小的下降路径是 [1,4,7]，所以答案是 12。

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)] 
        dp[-1] = A[-1]
        for i in range(n-2,-1,-1):
            for j in range(0,n):
                #左边界
                if j-1 < 0:
                    dp[i][j] = A[i][j] + min(dp[i+1][j],dp[i+1][j+1])
                #右边界
                elif j+1 == n:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1],dp[i+1][j])
                #中间
                else:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])
        return min(dp[0])