class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp={}
        dp[0]=dp[1]=1
        for i in range(2, n+1):
            if i in dp:
                return dp[i]
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
