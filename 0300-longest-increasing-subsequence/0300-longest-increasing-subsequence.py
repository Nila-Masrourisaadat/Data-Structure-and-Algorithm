class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        maxlen=0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
            maxlen=max(maxlen,dp[i])
        return maxlen
