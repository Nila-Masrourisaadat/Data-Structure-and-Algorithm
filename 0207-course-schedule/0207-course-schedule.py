class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj=collections.defaultdict(list)
        visit, cycle=set(),set()
        for ai,bi in prerequisites:
            adj[bi].append(ai)
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
                
            cycle.add(node)

            for child in adj[node]:
                if not dfs(child):
                    return False

            cycle.remove(node)
            visit.add(node)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
