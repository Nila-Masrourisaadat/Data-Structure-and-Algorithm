class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]



        def steps(n):
            if n==0 or n==1:
                return 1
            return steps(n-1)+steps(n-2)