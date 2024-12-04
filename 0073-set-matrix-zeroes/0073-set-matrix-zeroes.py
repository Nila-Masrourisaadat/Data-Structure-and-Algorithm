class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROWS,COLS=len(matrix),len(matrix[0])
        rows,cols=set(),set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]==0:
                    rows.add(r)
                    cols.add(c) 
        for r in range(ROWS):
            for c in range(COLS):
                if r in rows or c in cols:
                    matrix[r][c]=0

        
        

