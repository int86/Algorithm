#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 513. 找树左下角的值 难度：中等
# 给定一个二叉树，在树的最后一行找到最左边的值。

# 示例 1:

# 输入:

#     2
#    / \
#   1   3

# 输出:
# 1
 

# 示例 2:

# 输入:

#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7

# 输出:
# 7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans,self.maxlevel = 0,0
        def dfs(node,deep):
            if not node:
                return
            dfs(node.left,deep+1)
            if deep>self.maxlevel:
                self.ans = node.val
                self.maxlevel = deep
            dfs(node.right,deep+1)
        dfs(root,1)
        return self.ans
