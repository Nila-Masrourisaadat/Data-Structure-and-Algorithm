class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        l,r=0,0
        chars=set()
        while r<len(s):
            if s[r] not in chars:#not repeated character
                chars.add(s[r])
                max_len=max(max_len, r-l+1)
                r+=1
            else:#if repeated keep shrinking
                chars.remove(s[l])
                l+=1
        return max_len