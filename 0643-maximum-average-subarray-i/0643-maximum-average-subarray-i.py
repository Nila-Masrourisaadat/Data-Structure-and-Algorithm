class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum=0
        for i in range(k):
            sum+=nums[i]
        if len(nums)==1:
            return sum
        l,r=1,k
        avg=sum
        while r<len(nums):
            sum+=nums[r]
            sum-=nums[l-1]
            avg=max(avg,sum)
            l+=1
            r+=1
        return float(avg)/k

    