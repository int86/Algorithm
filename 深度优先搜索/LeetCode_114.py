#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 114. 二叉树展开为链表 难度：中等
# 给定一个二叉树，原地将它展开为链表。

# 例如，给定二叉树

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

class Solution(object):
    def __init__(self):
        self.pre = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right,root.left,self.pre = self.pre,None,root