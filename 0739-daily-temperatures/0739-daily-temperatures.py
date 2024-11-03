class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # monotonic decreasing stack
        stack=[]
        output=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                output[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            stack.append([temp,i])

        return output
            