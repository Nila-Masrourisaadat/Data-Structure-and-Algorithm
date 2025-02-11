class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        ROWS,COLS=len(maze),len(maze[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=collections.deque()
        visit=set()
        steps=0

        q.append((entrance[0],entrance[1]))
        visit.add((entrance[0],entrance[1]))
        while q:
            steps+=1
            for _ in range(len(q)):
                row,col=q.popleft()

                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r,c) not in visit and r in range(0,ROWS) and c in range(0,COLS) and maze[r][c]==".":
                        if r==0 or c==0 or r==ROWS-1 or c==COLS-1: #border
                            return steps
                        q.append((r,c))
                        visit.add((r,c))
        
        return -1