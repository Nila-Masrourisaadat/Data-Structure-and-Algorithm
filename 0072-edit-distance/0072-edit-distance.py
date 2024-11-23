class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #memoization and recursive
        # dp={}

        # def dfs(i,j):
        #     if j==len(word2):
        #         return dp(i,j)
        #     if (i,j) in dp:
        #         return dp[(i,j)]

        #     if i<len(words1) and j<len(words2) and word1[i]==word2[j]:
        #         return dp(i+1,j+1)
        #     elif i<len(words1) and j<len(words2):
        #         dp[(i,j)]=min(dp(i+1,j),dp(i,j+1),dp(i+1,j+1))+1
        #     return dp[(i,j)]
        
        # return dfs(0,0)

        #bottom up and iterative
        dp=[[float("inf")]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        for j in range(len(word2)+1):
            dp[len(word1)][j]=len(word2)-j
        for i in range(len(word1)+1):
            dp[i][len(word2)]=len(word1)-i

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
                
        return dp[0][0]
            