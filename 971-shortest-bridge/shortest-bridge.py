class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # bfs to find one of the islands first

        ROWS,COLS=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        island=set()
        found=False
        def dfs(row,col):
            if (row,col) in island:
                return 
            island.add((row,col))
            for dr,dc in directions:
                r,c=row+dr,col+dc
                if r in range(ROWS) and c in range(COLS) and grid[r][c]==1:
                    dfs(r,c)

        #now that we've found all the lands in one of the islands stored in visit set:
        #bfs from this island to the other one and marking the steps
        
        def bfs():
            q = collections.deque(island)
            steps=0
            while q:
                for _ in range(len(q)):
                    row,col=q.popleft()

                    for dr, dc in directions:
                        r,c=row+dr,col+dc

                        if r in range(0,ROWS) and c in range(0,COLS) and (r,c) not in island:
                            if grid[r][c]==0:
                                q.append((r,c))
                                island.add((r,c))
                            else:#that means its the new island
                                return steps
                steps+=1


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==1:
                    dfs(row,col)
                    q = collections.deque(island)
                    return bfs()

        

   
            