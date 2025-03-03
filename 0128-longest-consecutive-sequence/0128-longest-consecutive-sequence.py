class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_set=set(nums)
        max_n=0
        for num in nums_set:
            if num-1 not in nums_set: # then num isnt the start of the sequence
                n=num
                cnt=1
                while n+1 in nums_set:
                    cnt+=1
                    n+=1
                max_n=max(cnt,max_n) 
        return max_n
