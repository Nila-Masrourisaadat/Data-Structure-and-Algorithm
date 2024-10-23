class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        #we dont have cycles because a!=b and we have non negative weights->shortest path algo
        #to make this problem shortest path and to be able to use Dijkstra to find max probability is equal to find min 1/proability
        #create distance dictionary for d[v] and initialize all except source node with inf value
        d={node:float('inf') for node in range(n)}
        d[start_node]=-1

        #create min-heap
        q=[(-1,start_node)]# maybe i should initialize all the vertices with inifinity
        heapq.heapify(q)

        #visit set for the nodes we have processed and calculated the shortest path to
        visit=set()

        #create adjacency list
        adj=collections.defaultdict(list)
        for i,(u,v) in enumerate(edges):
            w=succProb[i]
            adj[u].append([w,v])
            adj[v].append([w,u])#because undirected
        
        while q:
            sp,u=heapq.heappop(q)
            visit.add(u)
            if u==end_node:
                return sp*-1

            for w,v in adj[u]:
                if d[v]>=sp*w:#do log of those proability cuz multiplication of probs is addition of logs of them
                    d[v]=sp*w
                    if v not in visit:########thissssss
                        heapq.heappush(q,(d[v],v))

       
        return 0

        #time complexity= O(vlogv+E)