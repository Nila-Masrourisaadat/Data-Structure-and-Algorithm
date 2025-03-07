class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        q=collections.deque()
        islands=0
        visit=set()

        def bfs(row,col):
            q.append((row,col))
            visit.add((row,col))
            while q:
                row,col=q.popleft()
                
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c]=="1":
                        q.append((r,c))
                        visit.add((r,c))




        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]=="1" and (row,col) not in visit:
                    bfs(row,col)
                    islands+=1
        return islands