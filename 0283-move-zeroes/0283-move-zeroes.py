class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
      
        l,r=0,0
        while  l<len(nums):
            # while nums[l]!=0 and l<len(nums)-1:
            #     l+=1
            #if l is pointing at zero, r should go until finding non zero starting from l
            r=l
            while nums[r]==0 and r<len(nums)-1:
                r+=1
            #here l is pointing at zero and r has found next non zero
            #swap
            nums[r],nums[l]=nums[l],nums[r]
            #after the swap we move l to where r is and go from there
            l+=1
        return nums