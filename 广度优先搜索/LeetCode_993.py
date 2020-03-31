#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 993. 二叉树的堂兄弟节点 难度：简单
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。

# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。

# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。

 

# 示例 1：


# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 示例 2：


# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        height , parents = {} , {}
        def dfs(node,par=None):
            if node:
                height[node.val] = 1 + height[par.val] if par else 0
                parents[node.val] = par
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        return height[x] == height[y] and parents[x] != parents[y]