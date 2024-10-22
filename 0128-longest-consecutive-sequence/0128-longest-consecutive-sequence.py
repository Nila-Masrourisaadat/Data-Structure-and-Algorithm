class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #input: unsorted array int of nums
        #output: length of the longest consecutive elements sequence
        #time complexity o(n)
        #what if we create an array with size of the max(nums) and run through nums and put the numbers in the indexes of array and run through that new array one more time and everytime we encounter inconsistency thats not the sequence, the longest we can go without inconsistency is the answer but this is low key giving sorting so why not sort but sort is O(nlogn) but what im saying is bucket sort

        #hashset or hashmap to group them
        visit=set(nums)
        cnt=0
        res=0
        for num in nums:
            if num-1 not in visit:#only if it start of a sequence
                cnt+=1
                while num+1 in visit:
                    cnt+=1
                    num+=1
            res=max(cnt,res)
            cnt=0
        return res
           
