class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visit=set()
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        ROW,COL=len(grid),len(grid[0])
        islands=0
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row,col=q.popleft()
                
                for dr, dc in directions:
                    r,c=row+dr,col+dc
                    if (r,c) not in visit and 0<=r<ROW and 0<=c<COL and grid[r][c]=="1":
                        q.append((r,c))
                        visit.add((r,c))
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in visit and grid[i][j]=="1":
                    bfs(i,j)
                    islands+=1
        return islands