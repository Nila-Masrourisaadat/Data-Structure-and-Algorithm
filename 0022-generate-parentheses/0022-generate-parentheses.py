class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        #The function does not "restart" from the beginning when it backtracks. Instead, it resumes from the next line after the last recursive call. 
        def backtrack(chars, open_cnt,close_cnt):
            if open_cnt==close_cnt==n:
                res.append(chars)
                return
            if open_cnt<n:
                backtrack(chars+"(",open_cnt+1,close_cnt)
            if close_cnt<open_cnt:
                backtrack(chars+")",open_cnt,close_cnt+1)

        backtrack("",0,0)
        return res            
        