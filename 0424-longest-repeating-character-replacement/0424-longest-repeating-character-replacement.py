class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        l,r=0,0
        res=0
        while r<len(s) :
            count[s[r]] = count.get(s[r], 0) + 1
            while r-l+1-max(count.values())>k:#shrinking
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
            

        return res