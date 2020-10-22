#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 面试题 16.19. 水域大小  难度：中等
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

# 示例：

# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
# 提示：

# 0 < len(land) <= 1000
# 0 < len(land[i]) <= 1000

class Solution(object):
    def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        if not land:
            return []
        n,m ,ans= len(land),len(land[0]),[]
        queue = []

        def neighbor(i,j):   
            for nr,nc in [[i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i-1,j+1],[i+1,j-1],[i+1,j+1]]:
                if 0<=nr<n and 0<=nc<m and land[nr][nc]==0:
                    yield nr,nc

        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    queue.append([i,j])
                    land[i][j] = -1
                    num = 1
                    while queue:
                        nr,nc = queue.pop(0) 
                        for ii,jj in neighbor(nr,nc):
                            land[ii][jj] = -1
                            queue.append([ii,jj])
                            num += 1
                    ans.append(num)   

        return sorted(ans)