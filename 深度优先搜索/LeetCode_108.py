#!/usr/bin/python
# -*- coding: UTF-8 -*-

108. 将有序数组转换为二叉搜索树  难度：简单
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(start,end,nums):
            if start == end:
                return 
            mid = (start+end)>>1
            root = TreeNode(nums[mid])
            root.left = dfs(start,mid,nums)
            root.right = dfs(mid+1,end,nums)
            return root 

        return dfs(0,len(nums),nums)
