class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        provinces=0
        ROWS,COLS=len(isConnected), len(isConnected[0])
        Adj=collections.defaultdict(list)
        visit=set()
        q=collections.deque()
        for i in range(ROWS):
            for j in range(i,COLS): 
                if isConnected[i][j]==1:
                    Adj[i].append(j)
                    Adj[j].append(i)
        def bfs(row,col):
            q.append(row)

            while q:
                row=q.popleft()
                
                for city in Adj[row]:
                    if city not in visit:
                        q.append(city)
                        visit.add(city)


        for i in range(ROWS):
            for j in range(i,COLS): 
                if i not in visit:
                    bfs(i,j)
                    provinces+=1
        print(visit)
        return provinces if len(visit)==ROWS else provinces+ROWS-len(visit)