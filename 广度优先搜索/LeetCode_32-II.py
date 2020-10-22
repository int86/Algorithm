#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 面试题32 - II. 从上到下打印二叉树 II  难度：简单
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        stack ,ans= [root] ,[]
        while stack != []:
            tmp = []
            for _ in range(len(stack)):
                if stack==[]:
                    break
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(tmp)
        return ans