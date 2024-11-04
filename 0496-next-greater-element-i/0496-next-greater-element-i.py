class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1idx={}
        for i, num in enumerate(nums1):
            num1idx[num]=i
        
        stack=[]
        output=[-1]*len(nums1)
        for i , num in enumerate(nums2):
            while stack and stack[-1]<num:
                output[num1idx[stack[-1]]]=num
                stack.pop()
            if num in num1idx:
                stack.append(num)
        
        return output