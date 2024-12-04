class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output=[]
        visit=set()
        ROWS,COLS=len(matrix),len(matrix[0])
        def spiral(i,j):
            #top row
            for c in range(i,j):
                print("1",(i,c),matrix[i][c])
                if (i,c) in visit:
                    continue
                else:
                    visit.add((i,c))
                    output.append(matrix[i][c])
                    # output.append(matrix[i][:-1])

            #right most column
            for r in range(i,ROWS):
                print("2",(r,j),matrix[r][j])
                if (r,j) in visit:
                    continue
                else:
                    visit.add((r,j))
                    output.append(matrix[r][j]) 

            #bottom row
            for c in range(COLS-1,-1,-1):
                print("3",(ROWS-1-i,c),matrix[ROWS-1-i][c])
                if (ROWS-1-i,c) in visit:
                    continue
                else:
                    visit.add((ROWS-1-i,c))
                    output.append(matrix[ROWS-1-i][c])
                    # output.append(matrix[ROWS-1-i][::-1])#reverse order

            # #left most column
            for r in range(ROWS-2-i,i,-1):
                if (r,i) in visit:
                    continue
                else:
                    visit.add((r,i))
                    output.append(matrix[r][i])
        

        if ROWS==1:
            return matrix[0]
        for i in range(ROWS-1):
            j=COLS-1-i
            if j>=0:
                spiral(i,j)
        print(visit)
        return output

            



