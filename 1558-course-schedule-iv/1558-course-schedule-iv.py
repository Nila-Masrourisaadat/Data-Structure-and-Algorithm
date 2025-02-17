import collections

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Build adjacency list
        Adj = collections.defaultdict(list)
        for u, v in prerequisites:
            Adj[u].append(v)

        # Memoization dictionary (shared across all queries)
        dp = {}

        def dfs(u, v):
            if v in Adj[u]:  # Direct prerequisite
                return True
            if (u, v) in dp:  # Memoization check
                return dp[(u, v)]

            for child in Adj[u]:  # Explore all children
                if dfs(child, v):
                    dp[(u, v)] = True  # ✅ Store result
                    return True

            dp[(u, v)] = False  # ✅ Store negative result to avoid recomputation
            return False

        # Answer queries using memoized DFS
        return [dfs(u, v) for u, v in queries]
