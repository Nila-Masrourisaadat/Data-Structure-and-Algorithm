class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #bottom up recursive
        # dp=[0]*(n+1)
        # dp[0]=1
        # dp[1]=1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        
        # return dp[n]

        #top-down memoization
        dp=[-1]*n
        def steps(i):
            if i>=n:
                return i==n
            if dp[i]!=-1:
                return dp[i]
            dp[i]=steps(i+1)+steps(i+2)
            return dp[i]
        return steps(0)