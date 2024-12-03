class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        index={}
        for i,char in enumerate(s):
            index[char]=i
        size=0
        end=0
        res=[]
        for i,char in enumerate(s):
            end=max(end,index[char])
            size+=1
            if i==end:
                res.append(size)
                size=0
        return res




        