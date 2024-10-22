class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic={}
        for i, n in enumerate(nums):
            rem=target-n
            if rem in dic:
                return[i,dic[rem]]
            dic[n]=i
        return []
