class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        l,r=0,0
        if len(nums)==1:
            return [nums[0]**2]

        for i,num in enumerate(nums):
            if num>=0 and i!=0:
                l=i-1
                r=i
                break
        
        if l==r:
            l=len(nums)-1
            r=len(nums)
        
        while l>=0 and r<len(nums):
            left=nums[l]**2
            right=nums[r]**2
            if left<=right:
                res.append(left)
                l-=1
            else:
                res.append(right)
                r+=1

         # Append remaining left-side squares if any
        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1

        # Append remaining right-side squares if any
        while r < len(nums):
            res.append(nums[r] ** 2)
            r += 1
            
        return res
