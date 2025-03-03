class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l=0
        current_set=set()
        max_len=0
        for r in range(len(s)):
            #first remove the duplicates abcb
            while s[r] in current_set:
                current_set.remove(s[l])
                l+=1
            #now that we dont have duplicates we add the new char
            current_set.add(s[r])
            #now that we have a new substring we form the new substring and save the length
            max_len=max(max_len,len(current_set))  
        return max_len