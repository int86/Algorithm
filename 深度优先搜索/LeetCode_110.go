// 110. 平衡二叉树 难度：简单
// 给定一个二叉树，判断它是否是高度平衡的二叉树。

// 本题中，一棵高度平衡二叉树定义为：

// 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

// 示例 1:

// 给定二叉树 [3,9,20,null,null,15,7]

//     3
//    / \
//   9  20
//     /  \
//    15   7
// 返回 true 。

// 示例 2:

// 给定二叉树 [1,2,2,3,3,null,null,4,4]

//        1
//       / \
//      2   2
//     / \
//    3   3
//   / \
//  4   4
// 返回 false 。


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    if root == nil{
        return true
    }
    left := dfs(root.Left,0)
    right:=dfs(root.Right,0)
    if abs(left-right) > 1{
        return false
    }
    return isBalanced(root.Left) && isBalanced(root.Right)
}

func dfs(node *TreeNode,deep int)int{
    if node == nil{
        return deep
    }
    left := dfs(node.Left,deep+1)
    right :=dfs(node.Right,deep+1)
    return max(left,right)
}

func abs(a int)int{
    if a<0{
        return -a
    }
    return a
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
