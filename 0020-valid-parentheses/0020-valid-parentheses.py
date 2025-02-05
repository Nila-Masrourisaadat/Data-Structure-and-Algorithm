class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        stack=[]
        close_to_open={")":"(","}":"{","]":"["}
        for bracket in s:
            if bracket in close_to_open and stack:
                open_bracket=stack.pop()
                if open_bracket != close_to_open[bracket]:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
