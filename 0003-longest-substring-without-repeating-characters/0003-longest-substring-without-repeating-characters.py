class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        l = 0  # left pointer
        r = 0  # right pointer
        chars = set()

        # Loop until the right pointer reaches the end of the string
        while r < len(s):
            if s[r] not in chars:
                # Expand the window by adding the character at `r` to the set
                chars.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1  # Move the right pointer forward
            else:
                # Shrink the window from the left by removing the character at `l`
                chars.remove(s[l])
                l += 1  # Move the left pointer forward

        return max_len