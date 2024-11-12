class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums = [0,2,1,5,3,4]
        # ans=[0,1,2,4,5,3]
        # i=0
        # nums[0]=0
        # nums[nums[0]]=0
        # ans[0]=0
        # i=1
        # nums[1]=2
        # nums[nums[1]]=nums[2]=1
        # ans[1]=1
        # i=2
        # ans[2]=2
        # i=3
        # nums[3]=5
        # ans[3]=4
        # i=4
        # ans[4]=5
        # ans[5]=3
        ans=[0]*len(nums)
        for i, num in enumerate(nums):
            ans[i]=nums[num]
        return ans

        
        
