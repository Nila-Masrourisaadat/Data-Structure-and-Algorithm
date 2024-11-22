class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #bottom up-iterative
        # dp=[ [False]*len(s1) for _ in range(len(s2)) ]
        # dp[len(s1)][:]=True
        # dp[len(s2)][:]=True

        # for i in range(len(s1)-1,-1,-1):
        #     for j in range(len(s2)-1,-1,-1):
        #         if s1[i]==s3[i+j] and (dp[i+1][j] or dp[i][j+1]):
        #             dp[i][j]=True
        #         if s2[j]==s3[i+j] and (dp[i+1][j] or dp[i][j+1]):
        #             dp[i][j]=True
                
        #         return False
        # return dp[0][0]

        #memoization and recursive
        dp={}
        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return i + j == len(s3)
            if (i,j) in dp:
                return dp[(i,j)]
            if i<len(s1)  and i+j<len(s3) and s1[i]==s3[i+j] and dfs(i+1,j):
                # dp[(i,j)]=True
                return True
            if j<len(s2) and i+j<len(s3) and s2[j]==s3[i+j] and dfs(i,j+1):
                return True
                # dp[(i,j)]=True #we dont have to cache cuz of this being dfs and going till the end of a path if one of the path is True then we return true and that's enough however we have to cache when its false so we dont go down that route again 
            dp[(i,j)]=False
            return False
        
        return dfs(0,0)