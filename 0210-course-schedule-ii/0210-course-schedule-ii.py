class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        if not prerequisites:
            for i in range(numCourses):
                res.append(i)
            return res
        
        #create adj list because prereq is techinically list of edges
        adj={c:[] for c in range(numCourses)}

        for a,b in prerequisites:
            adj[a].append(b)
        
        #dfs
        res=[]
        cycle,visit=set(),set()
        def dfs(node):
            if node in cycle:#we are visiting the node twice
                return False
            if node in visit:#node has been visited and added to the output, we dont need to visit it twice
                return True
            
            cycle.add(node)
            for child in adj[node]:
                if dfs(child)==False:
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return res

