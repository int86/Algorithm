#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 200. 岛屿数量 难度：中等
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def flood_fill(i,j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                flood_fill(i-1,j)
                flood_fill(i+1,j)
                flood_fill(i,j-1)
                flood_fill(i,j+1)

        if not grid:
            return 0
        grid = [['0'] + row + ['0'] for row in grid] 
        grid = [['0'] * len(grid[0])] + grid + [['0'] * len(grid[0])]
        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == '1':
                    count += 1
                flood_fill(i,j)
        return count