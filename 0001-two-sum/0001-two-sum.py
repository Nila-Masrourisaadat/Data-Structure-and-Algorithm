class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic={}
        for i,num in enumerate(nums):
            dic[num]=i
        for i,num in enumerate(nums):
            if target - num in dic and i!=dic[target-num]:
                return [i,dic[target-num]] 
    
