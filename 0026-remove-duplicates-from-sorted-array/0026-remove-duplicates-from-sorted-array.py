class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            

        l,r=0,0
        while r<len(nums):
            if nums[l]!=nums[r]:#found a new unique one
                if l<len(nums)-1:
                    nums[l+1]=nums[r]
                l+=1
                
            else:
                r+=1
        
        return l+1

        # [0,1,2,1,2]
        # l=2
        # r=4
        # [0,0]
        # l=0
        # r=1