class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rotten=collections.deque()
        visit=set()
        minutes=0     

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    rotten.append((i,j))
                    visit.add((i,j))
        
        while rotten:
            minutes+=1
            for _ in range(len(rotten)):
                row,col=rotten.popleft()

                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c]==1:
                        rotten.append((r,c))
                        visit.add((r,c))
                        grid[r][c]=2

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    return -1
        return minutes-1 if minutes!=0 else 0


