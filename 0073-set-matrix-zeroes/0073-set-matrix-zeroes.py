class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #better with O(1) space complexity
        ROWS,COLS=len(matrix),len(matrix[0])
        FirstRow=False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        FirstRow=True
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        
        #first column seperately
        if matrix[0][0]==0:# this condition is enough because if in column 0 anything was zero matrix[0][0] would have changed to zero
            for r in range(ROWS):
                matrix[r][0]=0
        #first row seperately
        if FirstRow:
            for c in range(COLS):
                matrix[0][c]=0



        
        #mine with O(m+n) space complexity
        # ROWS,COLS=len(matrix),len(matrix[0])
        # rows,cols=set(),set()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c]==0:
        #             rows.add(r)
        #             cols.add(c) 
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if r in rows or c in cols:
        #             matrix[r][c]=0

        
        

