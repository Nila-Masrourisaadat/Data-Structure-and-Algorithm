class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N=len(nums)
        B=[0]*len(nums)
        bitnums=[]
        def generatebitnums(i,B,bitnums):
            if i==N:
                bitnums.append(B[:])
                return
            
            #for including the element
            B[i]=1
            generatebitnums(i+1,B,bitnums)

            #for not including the element
            B[i]=0
            generatebitnums(i+1,B,bitnums)

        
        

        generatebitnums(0,B,bitnums)
        result=[]
        for nums2 in bitnums:
            subset=[]
            for i,num in enumerate(nums2):
                if num==1:
                    subset.append(nums[i])
            result.append(subset)
        
        return result
            