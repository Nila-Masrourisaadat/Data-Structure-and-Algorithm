class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevmap={}
        res=[]
        for i, num in enumerate(nums):
            diff=target-num
            if diff in prevmap:
                res=[i,prevmap[diff]]
            prevmap[num]=i
        return res