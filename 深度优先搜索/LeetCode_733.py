#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 733. 图像渲染  难度：简单
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

# 最后返回经过上色渲染后的图像。

# 示例 1:

# 输入: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        target,visted,n,m = image[sr][sc],[],len(image),len(image[0])
        def dfs(i,j,target):
            if (i,j) not in visted:
                visted.append((i,j))
                if image[i][j] == target:
                    image[i][j] = newColor
                if i-1 >=0 and image[i-1][j]==target:
                    dfs(i-1,j,target)
                if i+1 < n and image[i+1][j]==target:
                    dfs(i+1,j,target)
                if j-1 >=0 and image[i][j-1]==target:
                    dfs(i,j-1,target)
                if j+1 <m and image[i][j+1]==target:
                    dfs(i,j+1,target)
            else:
                return 
        dfs(sr,sc,target)        
        return image
