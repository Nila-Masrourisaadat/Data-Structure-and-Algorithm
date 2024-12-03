class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        minleft=0
        maxleft=0
        for i, par in enumerate(s):
            if par=="(":
                minleft+=1
                maxleft+=1
            elif par=="*":
                maxleft+=1
                #when we want to consider it as ")"
                minleft-=1
            else:#when encountering ")"
                maxleft-=1
                minleft-=1
            if maxleft<0:
                return False
            if minleft<0:
                minleft=0
        return True if 0 in range(minleft,maxleft+1) else False
            

                      
