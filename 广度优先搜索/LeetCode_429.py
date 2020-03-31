#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 429. N叉树的层序遍历 难度：中等
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

# 例如，给定一个 3叉树 :

 



 

# 返回其层序遍历:

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        def helper(node,lever,res):#子节点，深度，存储栈
            lever += 1  #每次递归，深度加1
            if (len(res) - 1 < lever):
                res.append([]) #
            for i in node:  #遍历孩子节点
                res[lever].append(i.val)
                if i.children is not None: #如果子节点还有子节点，递归调用
                    helper(i.children,lever,res)
        res.append([root.val]) #记录第一个祖先节点，深度为0
        helper(root.children,0,res)
        res.pop()
        return res