#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 559. N叉树的最大深度 难度：中等
# 给定一个 N 叉树，找到其最大深度。

# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

# 例如，给定一个 3叉树 :

 



 

# 我们应返回其最大深度，3。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(x) for x in root.children]
        return max(height)+1
