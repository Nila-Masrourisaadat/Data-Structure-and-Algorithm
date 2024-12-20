class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        # dp={}
        # dp[0]=nums[0]
      
        #recusrive memoization
        # def HR(i):
        #     if i==1:
        #         dp[1]= max(nums[0],nums[1])
        #         return dp[1]
        #     if i in dp:
        #         return dp[i]
        #     dp[i]=max(HR(i-2)+nums[i],HR(i-1))
        #     return dp[i]
        # return HR(len(nums)-1)


        #iterative bottom up
        first=nums[0]
        second=max(first,nums[1])
        for i in range(2,len(nums)):
            first,second=second,max(second, first+nums[i])
        return second
            