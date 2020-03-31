#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 面试题32 - I. 从上到下打印二叉树 难度：中等
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：

# [3,9,20,15,7]

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
        :rtype: List[int]
        """
        queue,ans = [root],[]
        if not root:
            return ans
        while  queue:
            if queue==[]:
                break
            node  =  queue.pop(0)
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans