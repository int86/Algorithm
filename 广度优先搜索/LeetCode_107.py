#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 107. 二叉树的层次遍历 II
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：

# [
#   [15,7],
#   [9,20],
#   [3]
# ]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res = []
        def bfs(root,d):
            if not root:
                return
            if len(res) == d:
                res.insert(0,[])
            res[-(d+1)].append(root.val)
            # print res
            bfs(root.left,d+1)
            bfs(root.right,d+1)
        bfs(root,0)
        return res