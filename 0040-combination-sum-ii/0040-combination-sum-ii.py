class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        def dfs(i,subset,sum):
            if i>=len(candidates) or sum>=target:
                if sum==target:
                    res.append(subset[:])
                return
            #choose
            subset.append(candidates[i])

            #explore
            dfs(i+1,subset,sum+candidates[i])

            #unchoose
            candidate=subset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,subset,sum)
            

        dfs(0,[],0)
        return res
