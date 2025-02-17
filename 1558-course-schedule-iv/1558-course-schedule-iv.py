class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        #dfs
        #recursion
        #Adj list
        answer=[]
        Adj=collections.defaultdict(list)
        for u,v in prerequisites:
            Adj[u].append(v)
        def dfs(u,v,dp):
            if (u,v) in dp:
                return dp[(u,v)]
            if v in Adj[u]:
                return True 
            for child in Adj[u]:
                if dfs(child, v,dp):
                    dp[(u,v)]=True
                    return True
            dp[(u,v)]=False
            return False

        dp={}
        for u,v in queries:
            answer.append(dfs(u,v,dp))
        
        return answer