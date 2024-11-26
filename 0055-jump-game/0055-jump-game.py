class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        r=len(nums)-2
        goal=len(nums)-1
        while r>=0:
            if goal<=r+nums[r]:
                goal=r
            r-=1
        return True if not goal else False

            

