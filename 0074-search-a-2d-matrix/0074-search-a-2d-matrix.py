class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #sorted: it kinda is like a m*n one dimensional array
        ROWS,COLS=len(matrix),len(matrix[0])
        l,r=0,ROWS*COLS-1
        while l<=r:
            mid=l+(r-l)//2
            mid_r=mid//COLS
            mid_c=mid%COLS
            if matrix[mid_r][mid_c]<target:
                l=mid+1
            elif matrix[mid_r][mid_c]>target:
                r=mid-1
            else:
                return True
        return False