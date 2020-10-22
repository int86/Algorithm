#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 892. 三维形体的表面积  难度：简单
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

# 请你返回最终形体的表面积。

 

# 示例 1：

# 输入：[[2]]
# 输出：10
# 示例 2：

# 输入：[[1,2],[3,4]]
# 输出：34
# 示例 3：

# 输入：[[1,0],[0,2]]
# 输出：16
# 示例 4：

# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
# 示例 5：

# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ans ,overlapping = 0,0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ans += (4 * grid[i][j] + 2)
                if j+1 < n:
                    overlapping += min(grid[i][j],grid[i][j+1]) #从左到右
                if j-1 >= 0:
                    overlapping += min(grid[i][j],grid[i][j-1]) #从右到左
                if i+1 < n:
                    overlapping += min(grid[i][j],grid[i+1][j]) #从上到下
                if i-1 >= 0:
                    overlapping += min(grid[i][j],grid[i-1][j]) #从下到上
        return ans-overlapping


#优化版本
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ans ,overlapping = 0,0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ans += (4 * grid[i][j] + 2)
                if j+1 < n:
                    overlapping += (min(grid[i][j],grid[i][j+1]))*2 #从左到右
                if i+1 < n:
                    overlapping += (min(grid[i][j],grid[i+1][j]))*2 #从上到下
        return ans-overlapping