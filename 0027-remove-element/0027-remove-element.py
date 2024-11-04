class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]!=val:
                l+=1
                continue
            if nums[r]==val:
                r-=1
                continue
            tmp=nums[l]
            nums[l]=nums[r]
            nums[r]=tmp
            l+=1
            r-=1
        if nums[l]!=val:
            return l+1
        return l
        
