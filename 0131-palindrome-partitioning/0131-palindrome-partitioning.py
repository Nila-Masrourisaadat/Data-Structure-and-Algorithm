class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def ispalindrome(subset,l,r):
            while l<r:
                if subset[l]!=subset[r]:
                    return False
                else:
                    r-=1
                    l+=1
            return True
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(s):
                res.append(subset[:])
                return
            for j in range(i,len(s)):
                if ispalindrome(s,i,j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
            
        dfs(0)
        return res

















