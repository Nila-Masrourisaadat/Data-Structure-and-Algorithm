class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_to_open={")":"(","]":"[","}":"{"}
        stack=[]
        for char in s:
            if char in close_to_open:
                if stack and stack[-1]==close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False