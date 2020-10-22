#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 897. 递增顺序查找树
# 给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

 

# 示例 ：

# 输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \ 
# 1        7   9

# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
                 9  

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        res = cur = TreeNode(None)
        for c in stack:
            cur.right = TreeNode(c)
            cur = cur.right
        return res.right
