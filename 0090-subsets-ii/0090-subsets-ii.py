class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res=[]
        # subset=[]
        # def dfs(i):
        #     if i>=len(nums):
        #         subset.sort()
        #         if subset not in res:
        #             res.append(subset[:])
        #         return

        #     subset.append(nums[i])
        #     dfs(i+1)

        #     subset.pop()
        #     dfs(i+1)
        
        # dfs(0)
        # return res

        nums.sort()
        def generatebits(i,B,Bits):
            if i==len(nums):
                Bits.append(B[:])
                return
            
            B[i]=0
            generatebits(i+1,B,Bits)

            B[i]=1
            generatebits(i+1,B,Bits)

        B=[0]*len(nums)
        Bits=[]
        res=[]
        generatebits(0,B,Bits)

        for B in Bits:
            subset=[]
            for i, b in enumerate(B):
                if b==1:
                    subset.append(nums[i])
            # subset.sort()
            if subset not in res:
                res.append(subset)
        return res
            
