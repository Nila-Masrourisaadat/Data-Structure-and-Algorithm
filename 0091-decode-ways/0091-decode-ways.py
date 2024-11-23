class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #bottom up
        dp={len(s):1}
        
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]=="0":
        #         dp[i]=0
        #     else:
        #         dp[i]=dp[i+1]
        #     if i<len(s)-1 and int(s[i]+s[i+1])<27 and s[i]!="0":
        #         dp[i]+=dp[i+2]
            
        # return dp[0]

        #memoization
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                dp[i]=0
                return 0
            dp[i]=dfs(i+1)
            if i<len(s)-1 and int(s[i]+s[i+1])<27 and s[i]!="0":
                dp[i]+=dfs(i+2)
            return dp[i]

        return dfs(0)

                


       