class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                res= min(nums[l],res)
                break
            mid=l+(r-l)//2
            res=min(res,nums[mid])
            #edge case where we are at a portion that is sorted or the array is sorted and not rotated
            if nums[mid]>=nums[l]: # we are in left portion
                l=mid+1 # we want to go to the right portion
            else:
                r=mid-1
                
        
        return res