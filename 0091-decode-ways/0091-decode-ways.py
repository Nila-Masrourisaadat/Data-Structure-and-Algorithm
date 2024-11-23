class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp={len(s):1}
        

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            #itself
            else:
                dp[i]=dp[i+1]
            #one before
            if i<len(s)-1 and int(s[i]+s[i+1])<27 and s[i]!="0":
                dp[i]+=dp[i+2]
            
        return dp[0]



                


       