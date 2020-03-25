#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 303. 区域和检索 - 数组不可变 难度：简单
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

# 示例：

# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

class NumArray(object):

    def __init__(self,nums):
        self.nums = nums
        if not nums:
            return 
        n = len(self.nums)
        self.dp = [0]*(n+1)
        self.dp[1]=nums[0]
        for i in range(2,n+1):
            self.dp[i] = nums[i-1]+self.dp[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1]-self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)