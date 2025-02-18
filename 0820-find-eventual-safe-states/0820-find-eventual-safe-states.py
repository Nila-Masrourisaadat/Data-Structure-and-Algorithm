class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        loop=set()
        dp={}
        def dfs(node):

            if node in dp:
                return dp[node]
            if node in terminal:
                return True
            if node in loop:
                return False
            loop.add(node)
            for child in graph[node]:
                if not dfs(child):
                    dp[node]=False
                    return False
            loop.remove(node)
            dp[node]=True
            return True

        terminal=set()
        for i in range(len(graph)):
            if not graph[i]:
                terminal.add(i)
        res=[]
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res
