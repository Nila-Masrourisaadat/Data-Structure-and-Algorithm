class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bit manipulation solution
        res=0
        for n in nums:
            res=res^n
        return res
        #sorting solution
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                 return nums[i]
        return nums[-1]