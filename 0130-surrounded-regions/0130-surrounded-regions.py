class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROWS,COLS=len(board),len(board[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row,col):
            if row==ROWS or row<0 or col==COLS or col<0 or board[row][col]!="O":
                return 
            board[row][col]="T"
            for dr, dc in directions:
                # if board[row+dr][col+dc]=="O":
                dfs(row+dr,col+dc)
                    

        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col]=="O" and (row in [0,ROWS-1] or col in [0,COLS-1])):#unsurrounded regions
                    dfs(row, col)


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]=="O":
                    board[row][col]="X"
                if board[row][col]=="T":
                    board[row][col]="O"
        
