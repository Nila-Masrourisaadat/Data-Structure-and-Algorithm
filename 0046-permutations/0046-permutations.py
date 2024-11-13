class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N=len(nums)
        # chosen=[0]*N
        chosen=[]
        res=[]
        def permutehelper(nums, chosen, res):
            if not nums or len(chosen)==N:
                res.append(chosen[:])
                return
            
            for i,num in enumerate(nums):
                #choose
                chosen.append(num)

                #explore (permute)
                permutehelper(nums[:i]+nums[i+1:],chosen,res)

                #unchoose (backtrack)
                chosen.pop()

        permutehelper(nums, chosen,res)
        return res