#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1315. 祖父节点值为偶数的节点和  难度：中等
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。

 

# 示例：



# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(g_val,p_val,node):
            if not node:
                return
            if g_val&1==0:
                self.ans += node.val
            dfs(p_val,node.val,node.left)
            dfs(p_val,node.val,node.right)
        dfs(1,1,root)
        return self.ans
