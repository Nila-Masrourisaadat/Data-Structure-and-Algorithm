class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        summ=0
        dp=set()
        dp.add(0)
        sumall=sum(nums)
        if sumall%2!=0:
            return False
        for i in range(len(nums)-1,-1,-1):
            for j in list(dp):
                summ=nums[i]+j
                dp.add(summ)
                if sumall-summ==summ:
                    return True
        return False