class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp={}
        dp[0]=0
        dp[1]=0
        for i in range(2,len(cost)):
            if i in dp:
                return dp[i]
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[len(cost)-1]

        #top down (from right)
        # for i in range(len(cost)-3,-1,-1):
        #     cost[i]=min(cost[i+1],cost[i+2])+cost[i]

        # return min(cost[0],cost[1])
        #bottom up (from left) 

       


        
        