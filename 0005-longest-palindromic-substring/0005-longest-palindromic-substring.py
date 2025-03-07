class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res=[[False] *len(s) for _ in range(len(s))]
        resLen,resIdx=0,0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i] == s[j] and (j - i <= 2 or res[i + 1][j - 1]):
                    res[i][j]=True
                    if resLen<(j-i+1):
                        resLen= j-i+1
                        resIdx=i
        return s[resIdx:resIdx+resLen]


   
        # resIdx, resLen = 0, 0
        # n = len(s)

        # dp = [[False] * n for _ in range(n)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             if resLen < (j - i + 1):
        #                 resIdx = i
        #                 resLen = j - i + 1

        # return s[resIdx : resIdx + resLen]