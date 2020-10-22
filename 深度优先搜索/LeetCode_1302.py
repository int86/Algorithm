#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1302. 层数最深叶子节点的和  难度：中等
# 给你一棵二叉树，请你返回层数最深的叶子节点的和。

 

# 示例：



# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        ld,rd = {},{}
        def dfs(node,deep,d):
            if not node:
                return
            if deep not in d:
                d[deep] = node.val
            else:
                d[deep] += node.val
            dfs(node.left,deep+1,d)
            dfs(node.right,deep+1,d)
        dfs(root.left,1,ld)
        dfs(root.right,1,rd)
        n,m = len(ld),len(rd)
        if n==m:
            return ld[n]+rd[m]
        elif n>m:
            return ld[n]
        else:
            return rd[m]
