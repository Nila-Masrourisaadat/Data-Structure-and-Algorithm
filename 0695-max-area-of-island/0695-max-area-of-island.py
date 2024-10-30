class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(m,n,visit):
            q=collections.deque()
            q.append((m,n))
            visit.add((m,n))
            cnt=1
            while q:
                row,col=q.pop()
                # if (row,col) in visit:
                #     continue
                # visit.add((row,col))
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if r==ROWS or c==COLS or r<0 or c<0 or grid[r][c]==0 or (r,c) in visit:
                        continue
                    
                    visit.add((r,c))
                    cnt+=1
                    print(r,c,cnt)
                    q.append((r,c))
            return cnt



        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        res=0
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        for m in range(ROWS):
            for n in range (COLS):
                if grid[m][n]==1:
                    res=max(res,bfs(m,n,visit))
        
        return res