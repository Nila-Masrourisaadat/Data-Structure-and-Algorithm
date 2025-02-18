class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        dp={}
        def dfs(node):
            #dp/memoization to avoid repeated searches and optimization
            if node in dp:
                return dp[node]
            if node in terminal:#when we find out that this path we are in is leading to terminal node
                return True
            dp[node]=False
            for child in graph[node]:
                if not dfs(child):#if only a path from only even one of the children doesnt lead to terminal then its False
                    dp[node]=False
                    return False
            dp[node]=True
            return True
        #finding the terminal nodes
        terminal=set()
        for i in range(len(graph)):
            if not graph[i]:
                terminal.add(i)
        #finding the safe nodes
        res=[]
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res





        # loop=set()
        # dp={}
        # def dfs(node):
        #     #dp/memoization to avoid repeated searches and optimization
        #     if node in dp:
        #         return dp[node]
        #     if node in terminal:#when we find out that this path we are in is leading to terminal node
        #         return True
        #     #cycle detection    
        #     if node in loop:
        #         return False
        #     loop.add(node)
        #     ####
        #     for child in graph[node]:
        #         if not dfs(child):#if only a path from only even one of the children doesnt lead to terminal then its False
        #             dp[node]=False
        #             return False
        #     loop.remove(node)# for cycle detection, have to remove the node from loop set after the dfs is complete
        #     dp[node]=True
        #     return True
        # #finding the terminal nodes
        # terminal=set()
        # for i in range(len(graph)):
        #     if not graph[i]:
        #         terminal.add(i)
        # #finding the safe nodes
        # res=[]
        # for i in range(len(graph)):
        #     if dfs(i):
        #         res.append(i)

        # return res
