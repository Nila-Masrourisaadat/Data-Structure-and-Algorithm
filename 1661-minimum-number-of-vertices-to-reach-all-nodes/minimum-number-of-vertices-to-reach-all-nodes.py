class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        Adj=collections.defaultdict(list)
        for a,b in edges:
            Adj[b].append(a)
            
        res=[]
        for i in range(n):
            if i not in Adj:
                res.append(i)

        return res