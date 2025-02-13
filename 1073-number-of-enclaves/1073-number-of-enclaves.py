class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #bfs
        ROWS,COLS= len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        visit=set()
        land,borderland=0,0
        def dfs(row,col):
            if row<0 or row ==ROWS or col<0 or col==COLS or (row,col) in visit or grid[row][col]==0 :
                return 0
            visit.add((row,col))
            cnt=1
            for dr,dc in directions:
                r,c=row+dr,col+dc
                cnt+=dfs(r,c)
            return cnt


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==1:
                    land+=1
                    if (row,col) not in visit and (row==0 or row==ROWS-1 or col==0 or col==COLS-1):#on the border
                        borderland+=dfs(row,col)
        return land - borderland


        # q=collections.deque()
        # lands=0
        # def bfs(row,col):
        #     q.append((row,col))
        #     visit.add((row,col))
        #     cnt=1
        #     while q:
        #         row,col=q.popleft()
                
        #         for dr,dc in directions:
        #             r,c=row+dr,col+dc
                    
        #             if grid[r][c]==1 and (r,c) not in visit:
        #                 if r==0 or r==ROWS-1 or c==0 or c==COLS-1:#on the border
        #                     return cnt
        #                 q.append((r,c))
        #                 visit.add((r,c))
        #                 cnt+=1
        #     #if we successfully traversed a land, then return number of lands in that move
        #     return cnt



        # for row in range(ROWS):
        #     for col in range(COLS):
                
        #             if grid[row][col]==1  and (row,col) not in visit: #bfs on the 1 s:lands and that its already not the border
        #                 if row!=0 or row!=ROWS-1 or col!=0 or col!=COLS-1:#if not on the border
        #                     lands+=bfs(row,col)
        # return lands
