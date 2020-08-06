"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=[['.']*n for _ in range(n)] #初始化二维棋盘
        print(board)
        res=[]

        def backtrack(board,row):
        #     if 满足条件:
        #         res.append(路径)
        #         return
            if row==len(board):
                tmp_list=[] #二维变一维添加到res中
                print board
                for e_row in board:
                    tmp=''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return
        #     for 选择 in 选择列表:
        #         做选择
        #         backtrack(路径,选择列表)
        #         撤销选择
            for col in range(len(board[0])):
                if not isValid(board,row,col):
                    # print(isValid(board,row,col))
                    continue
                board[row][col]='Q'
                # print(board)
                backtrack(board,row+1)
                board[row][col]='.'
    

        def isValid(board,row,col):
            n=len(board)
            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            r_row,r_col=row,col
            while r_row>0 and r_col<n-1:
                r_row-=1
                r_col+=1
                if board[r_row][r_col]=='Q':
                    return False
            # 检查左上方是否有皇后互相冲突
            l_row,l_col=row,col
            while l_row>0 and l_col>0:
                l_row-=1
                l_col-=1
                if board[l_row][l_col]=='Q':
                    return False
            return True


        backtrack(board,0)
        return res