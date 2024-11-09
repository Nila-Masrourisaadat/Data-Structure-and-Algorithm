class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            #left side
            if nums[0]<=nums[m]:
                if target<nums[0] or target>nums[m]:
                    l=m+1
                else:
                    r=m-1
            #right side
            else:
                if target>nums[r] or target<nums[m]:
                    r=m-1
                else:
                    l=m+1
        return -1
