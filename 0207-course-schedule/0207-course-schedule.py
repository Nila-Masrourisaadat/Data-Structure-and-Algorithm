class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        Adj=collections.defaultdict(list)
        for a,b in prerequisites:
            Adj[b].append(a)

        loop=set()
        visit=set()
        def dfs(n):
            if n in loop:# if we see the same node in a path then its a loop/cycle
                return False
            if n in visit:
                return True
            loop.add(n) # keeping track of the nodes in each path
            
            for pre in Adj[n]:
                if not dfs(pre):
                    return False
            loop.remove(n)
            visit.add(n)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True