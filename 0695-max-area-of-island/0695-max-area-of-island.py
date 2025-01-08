class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        visit=set()
        max_area=0
        area=0

        def bfs(r,c):
            print(r,c)
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            area=1
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc                    
                    if r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c]==1:
                        #its land that is part of an island
                        area+=1
                        q.append((r,c))
                        visit.add((r,c))
            return area



        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visit and grid[i][j]==1:
                    max_area=max(bfs(i,j),max_area)
        return max_area