class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # N=len(nums)
        # B=[0]*len(nums)
        # bitnums=[]
        # def generatebitnums(i,B,bitnums):
        #     if i==N:
        #         bitnums.append(B[:])
        #         return
            
        #     #for including the element
        #     B[i]=1
        #     generatebitnums(i+1,B,bitnums)

        #     #for not including the element
        #     B[i]=0
        #     generatebitnums(i+1,B,bitnums)

        
        

        # generatebitnums(0,B,bitnums)
        # result=[]
        # for nums2 in bitnums:
        #     subset=[]
        #     for i,num in enumerate(nums2):
        #         if num==1:
        #             subset.append(nums[i])
        #     result.append(subset)
        
        # return result
            

        #another shorter solution but same kinda algo or logic
        subset=[]
        res=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset[:])
                return 

            #including that element
            subset.append(nums[i]) 
            dfs(i+1)

            #not including that element
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res