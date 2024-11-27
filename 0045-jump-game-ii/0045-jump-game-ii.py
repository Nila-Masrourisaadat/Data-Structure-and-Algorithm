class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        l,r=0,0
        cnt=0
        tmp=0
        while r<len(nums)-1:
            cnt+=1
            for j in range(l,r+1):
                tmp=max(tmp,nums[j]+j)
            l=r+1
            r=tmp
        return cnt
        
            