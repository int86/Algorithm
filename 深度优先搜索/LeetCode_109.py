#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 109. 有序链表转换二叉搜索树  难度：中等
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定的有序链表： [-10, -3, 0, 5, 9],

# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        q = []
        while head:
            q.append(head.val)
            head = head.next

        def dfs(queue):
            if queue == []:
                return
            mid = len(queue)/2
            # if mid&1==0:
            #     mid = mid +1
            # print queue,mid,queue[mid]
            node = TreeNode(queue[mid])
            node.left = dfs(queue[:mid])
            node.right = dfs(queue[mid+1:])
            return node
        root = dfs(q)
        return root
