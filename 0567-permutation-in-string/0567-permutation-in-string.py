class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_dic={}
        for s in s1:
            s1_dic[s]=s1_dic.get(s,0)+1
        s1_dic2=s1_dic
        l,r=0,len(s1)-1
        while r<len(s2):
            s1_dic2=s1_dic.copy()
            for i,s in enumerate(s2[l:r+1]):
                # print(s2[l:r+1],s1_dic2)
                if s not in s1_dic2:
                    break
                if s1_dic2[s]>1:
                    s1_dic2[s]-=1
                elif s1_dic2[s]==1:
                    del s1_dic2[s]
                if not s1_dic2:
                    return True
                
            l+=1
            r+=1
        return False
