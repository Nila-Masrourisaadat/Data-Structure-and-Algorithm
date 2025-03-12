class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        for i in range(len(nums)-3,-1,-1):
            nums[i]=max(nums[i]+nums[i+2],nums[i+1])
        return max(nums[0],nums[1])