#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 872. 叶子相似的树 难度：简单
# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。



# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。

# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.s1,self.s2 = [],[]
        def helper(root,s):
            if not root:
                return 
            if not root.left and not root.right:
                s.append(root.val)
            helper(root.left,s)
            helper(root.right,s)
        helper(root1,self.s1)
        helper(root2,self.s2)
        return self.s1==self.s2
