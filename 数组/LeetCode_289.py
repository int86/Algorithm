#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 289. 生命游戏  难度：中等
# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

 

# 示例：

# 输入： 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# 输出：
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n,m = len(board),len(board[0])
        # copy = board
        copy = [[board[i][j] for j in range(m)] for i in range(n)]
        def neighbor(i,j):
            live,cell = 0,copy[i][j]
            for nr,nc in [[i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i-1,j+1],[i+1,j-1],[i+1,j+1]]:
                if (nr < n and nr >= 0) and (nc < m and nc >= 0):
                    if copy[nr][nc] == 1:
                        live += 1

            if cell==1 and (live < 2 or live > 3): #如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡,如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡
                board[i][j] = 0
            if cell == 0 and live == 3: #如果死细胞周围正好有三个活细胞，则该位置死细胞复活
                board[i][j] = 1
            return board[i][j]

        for i in range(n):
            for j in range(m):
                board[i][j] = neighbor(i,j)